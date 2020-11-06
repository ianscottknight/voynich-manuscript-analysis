import os
import dotenv
from pathlib import Path
import re


dotenv.load_dotenv()

# TODO: assign environmental variables
# VAR = os.getenv("VAR_NAME")


def get_package_dir():
    """Returns package directory based on hierarchical depth of util.py"""
    return Path(__file__).parent


PACKAGE_DIR = get_package_dir()

DATA_DIR = os.path.join(PACKAGE_DIR, "data")
DATA_RAW_DIR = os.path.join(DATA_DIR, "raw")
DATA_INTERIM_DIR = os.path.join(DATA_DIR, "interim")
DATA_PROCESSED_DIR = os.path.join(DATA_DIR, "processed")
DATA_EXTERNAL_DIR = os.path.join(DATA_DIR, "external")

MODELS_DIR = os.path.join(PACKAGE_DIR, "models")

VOYNICH_TEXT_PATH = f"{DATA_RAW_DIR}/voynich_transcription_eva.txt"


def load_txt_file_as_list(filepath):
    with open(filepath, "r") as f:
        lst = [line.strip() for line in f.readlines()]
    return lst


def get_paragraphs():

    lines = load_txt_file_as_list(VOYNICH_TEXT_PATH)
    paragraphs = []
    current_paragraph = []

    for line in lines:
        add = False
        s = "".join(line.split())

        if s[0] == "#":
            continue

        annotations = re.search("<(.*)>", s).groups()

        if ("." not in annotations[0]) or ("$" in annotations[1:]):
            add = True

        for annotation in list(set(annotations)):
            s = s.replace(f"<{annotation}>", ".")

        current_paragraph += [w for w in s.split(".") if w]

        if add:
            if len(current_paragraph) > 0:
                paragraphs.append(current_paragraph)
                current_paragraph = []

    return paragraphs


PARAGRAPHS = get_paragraphs()
WORDS = [word for paragraph in PARAGRAPHS for word in paragraph]
VOCAB = list(set(WORDS))
