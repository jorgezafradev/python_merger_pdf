# PDF WITH PYTHON
A simple Python application for merging PDF documents and applying watermarks using the PyPDF library.<br><br>
In order to use the library we need to install it using the following command:
```python
pip install pypdf
```
This project allows users to merge PDF files or apply a watermark by simply providing the names of the PDF documents.<br><br>
The application automatically locates the specified files, processes them according to the selected operation, and generates the resulting PDF without requiring the user to manually specify file paths.<br><br>
In order to do this we also use
```python
pathlib
```
## Pdf Merger
Python application that combines multiple PDF files into a single document.
```python
python3 pdf_merger.py file_1.pdf file_2.pdf ... file_x.pdf
```
the result is going to be stored in the `final_pdf/` folder with the name `merged_result.pdf`

## Pdf Watermark
Python application that add a watermark to all the files named.
```python
python3 pdf_water.py file_1.pdf file_2.pdf ... water_mark.pdf
```
the result is going to be stored in the `final_pdf/` folder and its going to save a new pdf per file inserted with the name `file_name_water.pdf`