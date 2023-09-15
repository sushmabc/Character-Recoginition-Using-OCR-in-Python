from flask import Flask, render_template, request
from PIL import Image
import pytesseract
import pdfplumber
import docx

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        uploaded_file = request.files["file"]

        if uploaded_file.filename != "":
            file_extension = uploaded_file.filename.rsplit(".", 1)[1].lower()

            if file_extension in ["jpg", "jpeg", "png"]:
                image = Image.open(uploaded_file)
                extracted_text = pytesseract.image_to_string(image)

            elif file_extension == "pdf":
                with pdfplumber.open(uploaded_file) as pdf:
                    extracted_text = ""
                    for page in pdf.pages:
                        extracted_text += page.extract_text()

            elif file_extension == "docx":
                doc = docx.Document(uploaded_file)
                extracted_text = ""
                for paragraph in doc.paragraphs:
                    extracted_text += paragraph.text + "\n"

            else:
                extracted_text = "Unsupported file format."

            return render_template("result.html", text=extracted_text)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
