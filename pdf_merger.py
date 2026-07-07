import sys
from pathlib import Path

from pypdf import PdfWriter

# constants
CURRENT_DIR = '.'
OUTPUT_PATH = "final_pdf/"
MERGED_NAME = "merged_result.pdf"


def find_path_of_file(pdf_file):
    location = None
    for path in Path(CURRENT_DIR).rglob(pdf_file):
        location = path.relative_to(CURRENT_DIR)
        break
    return location


def get_files():
    list_pdf_names = sys.argv[1:]
    list_files = []
    for file_name in list_pdf_names:
        location = find_path_of_file(file_name)
        list_files.append(location)
    return list_files


def merge_pdf(pdf_list):
    merger = PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write(f'{OUTPUT_PATH}/{MERGED_NAME}')


if __name__ == "__main__":
    output_folder = Path(OUTPUT_PATH)
    output_folder.mkdir(parents=True, exist_ok=True)
    files = get_files()
    merge_pdf(files)
