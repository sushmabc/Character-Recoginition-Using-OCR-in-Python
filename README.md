# Character-Recoginition-Using-OCR-in-Python

This repository contains a Python project for character recognition using Optical Character Recognition (OCR) techniques. The project includes code to recognize characters from various sources, including images, documents, and PDF files.

## Project Structure

The project is organized into the following files:

1. `ocrimage.py`: Python script to recognize characters from images using OCR.

2. `ocrdocx.py`: Python script to recognize characters from documents (DOCX) using OCR.

3. `ocrpdf.py`: Python script to recognize characters from PDF files using OCR.

4. `app.py`: Flask application that combines the three OCR scripts and provides a web-based user interface for character recognition. It also serves as the entry point to run the application.

## Running the Application

To run the application, follow these steps:

1. Ensure you have the required dependencies installed in your VS Code terminal:

   `pip install flask`
   
   `pip install pillow`

   `pip install pytesseract`

   `pip install pdfplumber`

   `pip install python-docx`

   

Start the Flask application by running the following command in your terminal:

      "python app.py"


Open your web browser and navigate to http://localhost:5000 to access the project's frontend.


## Frontend
The frontend of the project is built using HTML templates located in the templates folder. The CSS styles for the frontend can be found in the static folder.

## Usage
Upload an image, document (DOCX), or PDF file through the web interface.

Click the "Recognize Text" button to perform character recognition on the uploaded file.

View the recognized text on the web page.

## Contributing
If you would like to contribute to this project, feel free to submit a pull request. Contributions are always welcome!
