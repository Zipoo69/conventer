import tkinter as tk
from tkinter import filedialog
from pdf2docx import Converter

def convert():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return

    docx_path = pdf_path.replace(".pdf", ".docx")

    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

    status.config(text="Hotovo: " + docx_path)

root = tk.Tk()
root.title("PDF → DOCX converter")

btn = tk.Button(root, text="Vybrat PDF a převést", command=convert)
btn.pack(pady=20)

status = tk.Label(root, text="")
status.pack()

root.mainloop()