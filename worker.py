import sys
from pdf2docx import Converter
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn

pdf_path = sys.argv[1]
docx_path = sys.argv[2]

print("Converting:", pdf_path, "->", docx_path)
cv = Converter(pdf_path)
cv.convert(docx_path)
cv.close()

# Oprava fontu na Times New Roman
doc = Document(docx_path)
for para in doc.paragraphs:
    for run in para.runs:
        run.font.name = "Times New Roman"
        run.font.size = Pt(12)  # nastav velikost dle potřeby
doc.save(docx_path)

print("DONE")