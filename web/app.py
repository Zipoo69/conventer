from flask import Flask, request, render_template, send_file
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/convert", methods=["POST"])
def convert():
    file = request.files["file"]

    name = os.path.splitext(secure_filename(file.filename))[0]

    pdf_path = os.path.join(UPLOAD_FOLDER, name + ".pdf")
    docx_path = os.path.join(UPLOAD_FOLDER, name + ".docx")

    file.save(pdf_path)

    result = subprocess.run([
        "python",
        "worker.py",
        pdf_path,
        docx_path
    ], capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)

    if not os.path.exists(docx_path):
        return f"Konverze selhala:\n{result.stderr}", 500

    return send_file(docx_path, as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)