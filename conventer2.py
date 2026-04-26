import tkinter as tk
from tkinter import filedialog, ttk
from pdf2docx import Converter
import threading

def convert():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if not pdf_path:
        return

    docx_path = pdf_path.replace(".pdf", ".docx")

    progress.start()

    cv = Converter(pdf_path)
    cv.convert(docx_path)
    cv.close()

    progress.stop()
    status.config(text="Hotovo")

root = tk.Tk()
root.title("PDF → DOCX")

btn = tk.Button(root, text="Převést PDF", command=lambda: threading.Thread(target=convert).start())
btn.pack(pady=10)

progress = ttk.Progressbar(root, mode="indeterminate")
progress.pack()

status = tk.Label(root, text="")
status.pack()

root.mainloop()