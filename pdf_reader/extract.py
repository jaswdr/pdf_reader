import os

import PyPDF2

from pdf_reader.utils import DATA_DIR, PAGE_PATH, generate_path_id


def extract_pages(pdf_path):
    os.makedirs(DATA_DIR, exist_ok=True)
    filename = os.path.basename(pdf_path)
    book_id = generate_path_id(filename)

    pdf_reader = PyPDF2.PdfReader(open(pdf_path, "rb"))
    for page_num in range(len(pdf_reader.pages)):
        page_path = PAGE_PATH.format(book_id, page_num + 1)
        if os.path.exists(page_path):
            # page already extracted, skipping
            print(f"Page {page_num + 1} already extracted")
            continue

        with open(page_path, "w+") as f:
            page = pdf_reader.pages[page_num]
            f.write(page.extract_text())

        print(f"Page {page_num + 1} extracted")

    return book_id
