import docx

def extract_text_from_docx(docx_file_path):
    try:
        # Open the DOCX file
        doc = docx.Document(docx_file_path)

        # Initialize a variable to store the extracted text
        docx_text = ""

        # Iterate through paragraphs and extract text
        for paragraph in doc.paragraphs:
            docx_text += paragraph.text + "\n"

        return docx_text

    except Exception as e:
        return str(e)

# Replace 'your_docx_file.docx' with the path to your DOCX file
docx_file_path = 'D:/.My Projects/Technologics/my.docx'

# Call the function to extract text
extracted_text = extract_text_from_docx(docx_file_path)

# Print the extracted text
print(extracted_text)
