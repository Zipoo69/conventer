import sys
from pdf2docx import Converter

pdf_path = sys.argv[1]
docx_path = sys.argv[2]

print("Converting:", pdf_path, "->", docx_path)

cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()

print("DONE")