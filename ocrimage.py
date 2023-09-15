from PIL import Image
import pytesseract

# Open an image using PIL (Python Imaging Library)
image = Image.open("D:/.My Projects/Technologics/img1.jpg")

# Perform OCR on the image using pytesseract
text = pytesseract.image_to_string(image)

# Print the recognized text
print(text)
