import re
import hashlib

DATA_DIR = "./data/"
PAGE_PATH = DATA_DIR + "{}_page_{}.txt"


def generate_path_id(filename):
    hash = hashlib.md5()
    with open(filename, "rb") as f:
        hash.update(f.read(8192))

    return hash.hexdigest()


def chunkify(text):
    fixed_content = ""
    for line in text.split("\n"):
        if line[0].isupper() and fixed_content:
            fixed_content += ". " + line
            continue

        try:
            if line[0].isdigit() and fixed_content[-1].islower():
                fixed_content += " "
        except Exception:
            pass

        fixed_content += line

    end_of_paragraph = re.compile(r"\b\w+\.")
    last = 0
    chunks = []
    for match in end_of_paragraph.finditer(fixed_content):
        match_content = fixed_content[last : match.end()]
        match_content = match_content.strip()
        chunks.append(match_content)
        last = match.end()

    return chunks
