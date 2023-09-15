import pdfplumber

def extract_text_from_pdf(pdf_file_path):
    try:
        # Open the PDF file using pdfplumber
        with pdfplumber.open(pdf_file_path) as pdf:
            pdf_text = ""

            # Iterate through each page and extract text
            for page in pdf.pages:
                pdf_text += page.extract_text() + "\n"

        return pdf_text

    except Exception as e:
        return str(e)

# Replace 'your_pdf_file.pdf' with the path to your PDF file
pdf_file_path = 'D:/.My Projects/Technologics/my.pdf'

# Call the function to extract text
extracted_text = extract_text_from_pdf(pdf_file_path)

# Print the extracted text
print(extracted_text)
