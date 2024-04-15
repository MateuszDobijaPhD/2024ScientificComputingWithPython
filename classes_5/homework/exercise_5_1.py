# EXERCISE 5.1
#
# For a given directory (top) find the number of bytes taken by PDF files in the directory tree (".pdf" extensions). The code should be in the function find_pdf_size(top). In order to test the current directory we run find_pdf_size(".").


import os


def find_pdf_size(top):
    sumOfSizesOfPdfFiles = 0  # the number of PDF files
    for root, dirs, files in os.walk(top):  # walking top-down (default)
        for name in files:
            if name.lower().endswith(".pdf"):  # for *.PDF files
                sumOfSizesOfPdfFiles += os.path.getsize(os.path.join(root, name))
    return sumOfSizesOfPdfFiles



print("test:")
print("Number of bytes taken by PDF files in the current directory:", find_pdf_size("."))
