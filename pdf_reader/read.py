import os
import subprocess

import pyttsx3

from pdf_reader.utils import chunkify
from pdf_reader.utils import PAGE_PATH, generate_path_id

engine = pyttsx3.init()
engine.setProperty("voice", "english-us")
engine.setProperty("rate", 180)


def play_text_with_pyttsx3(text):
    engine.say(text)
    engine.runAndWait()


def play_text_with_festival(text):
    subprocess.Popen(
        ["festival", "--tts", "-b"],
        stdin=subprocess.PIPE,
    ).communicate(text.encode())


play_text = play_text_with_festival


def get_page_content(pdf_path, page_number):
    book_id = generate_path_id(pdf_path)
    file_to_read = PAGE_PATH.format(book_id, page_number)
    if not os.path.exists(file_to_read):
        print(f"Page {page_number} not found")
        return False

    with open(file_to_read, "r") as f:
        page_content = f.read()

    page_content = page_content.replace("\n", "").replace("  ", " ")
    return page_content


def read_page(page_content):
    for chunk in chunkify(page_content):
        print(chunk)
        print()
        play_text_with_festival(chunk)
