import os
import argparse

from pdf_reader.utils import chunkify
from pdf_reader.extract import extract_pages
from pdf_reader.read import get_page_content, read_page, play_text
from pdf_reader.summarize import summarize_page

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="pdf_reader", description="Text to speech utility for PDF files"
    )
    parser.add_argument("--pdf", required=True, help="Path to the PDF file to be read")
    parser.add_argument("--page", type=int, help="The page number to be read")

    args = parser.parse_args()

    if not os.path.exists(args.pdf):
        print(f"File {args.pdf} does not exist")
        exit(1)

    cmd = "extract"
    if args.page:
        cmd = "read"

    if cmd == "extract":
        extract_pages(args.pdf)
        exit(0)

    summary = None
    page_number = args.page

    while True:
        page_content = get_page_content(args.pdf, page_number)
        chunks = chunkify(page_content)
        for chunk in chunks:
            print(chunk)

        print("-" * 50)
        print(
            f"[Page: {page_number}] Next Page (Enter), [R]ead, [S]ummarize, [R]ead [S]ummary >> ",
            end="",
        )
        user_input = input()
        print()
        if user_input == "":
            page_number += 1
            continue
        if user_input == "s":
            summary = summarize_page(" ".join(chunks))
            print("=" * 50)
            print("Summary")
            print("=" * 50)
            print(summary)
        if user_input == "rs":
            if summary:
                for chunk in chunkify(summary):
                    print(chunk)
                    print()
                    play_text(chunk)
        if user_input == "r":
            read_page(page_content)
        if user_input == "exit" or user_input == "quit" or user_input == "q":
            break
        try:
            page_number = int(user_input.strip())
        except ValueError:
            pass
