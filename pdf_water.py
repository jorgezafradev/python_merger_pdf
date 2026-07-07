import sys
from pathlib import Path

from pypdf import PdfWriter, PdfReader

# constants
CURRENT_DIR = '.'
OUTPUT_PATH = "final_pdf/"
WATERED_NAME_EXTENSION = "_watered.pdf"


def find_path_of_file(pdf_file):
    location = None
    for path in Path(CURRENT_DIR).rglob(pdf_file):
        location = path.relative_to(CURRENT_DIR)
        break
    return location


def get_files():
    list_pdf_names = sys.argv[1:-1]
    list_files = []
    for file_name in list_pdf_names:
        location = find_path_of_file(file_name)
        list_files.append((file_name, location))
    return list_files


def add_water_mark(pdf_list_tuple, water_mark):
    stamp = PdfReader(water_mark).pages[0]
    for file_tuple in pdf_list_tuple:
        file_name, file_location = file_tuple
        writer = PdfWriter(clone_from=file_location)
        clean_name = file_name.split('.')[0]
        for page in writer.pages:
            page.merge_page(stamp, over=False)  # here set to False for watermarking
        writer.write(f'{OUTPUT_PATH}{clean_name}{WATERED_NAME_EXTENSION}')


if __name__ == "__main__":
    output_folder = Path(OUTPUT_PATH)
    output_folder.mkdir(parents=True, exist_ok=True)
    files = get_files()
    add_water_mark(files, sys.argv[-1])
