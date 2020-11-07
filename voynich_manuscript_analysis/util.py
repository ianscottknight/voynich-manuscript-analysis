import os
import dotenv
from pathlib import Path
import re
import collections


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


def get_paragraphs_dict():

    lines = load_txt_file_as_list(VOYNICH_TEXT_PATH)
    paragraphs_dict = collections.defaultdict(list)

    for line in lines:
        add = False
        s = "".join(line.split())

        annotations = re.search("<(.*)>", s).groups()
        annotation = annotations[0]

        pattern = (
            r"(f([0-9]+)([A-Za-z]+[0-9]*)?\.P([0-9]*[A-Za-z]*)\.([0-9]+[A-Za-z]*);H)"
        )

        match = re.match(pattern, annotation)
        if match == None:
            continue

        assert len(match.groups()) == 5

        annotation, folio, folio_qualifier, page_qualifier, line_number = match.groups()

        paragraph_id = f"f{folio}{folio_qualifier}.P{page_qualifier}"

        for annotation in list(set(annotations)):
            s = s.replace(f"<{annotation}>", ".")

        paragraph = [w for w in s.split(".") if w]

        if len(paragraph) > 0:
            paragraphs_dict[paragraph_id] += paragraph

    paragraphs_dict = collections.OrderedDict(
        sorted(paragraphs_dict.items(), key=lambda x: x[0])
    )

    return paragraphs_dict


PARAGRAPHS_DICT = get_paragraphs_dict()
WORDS = [word for paragraph in PARAGRAPHS_DICT.values() for word in paragraph]
VOCAB = list(set(WORDS))
