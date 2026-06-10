import pytesseract
import pymupdf
from pathlib import Path
from PIL import Image
import io

# Prep Image from pdf to png

path = Path("pdf")
image_path = Path("images")

def convert_pdf_to_png(pdf_path, output_folder, i):
    # opens pdf doc using pymudf library
    doc = pymupdf.open(pdf_path)
    # iterates through each page in the pdf
    for page_num in range(len(doc)):
        page = doc[page_num]
        # initializes zoom to clear up image for clarity
        mat = pymupdf.Matrix(2,2)
        
        # basically appliess a transformation onto a new canvas with the zoom
        pix = page.get_pixmap(matrix=mat)
        if Path(f"{output_folder}/receipt_{i}.png").is_file():
            print("File Exists already")
        else:
            pix.save(f"{output_folder}/receipt_{i}.png")
            print("File saved into images")
        print("completed conversion")

i = 1
# iterate through each item in directory
for file_path in path.iterdir():
    #print("complete 1")
    # checks if each item in the directory is not a subdirectory
    if file_path.is_file():
        #print("complete 2")
        convert_pdf_to_png(file_path, "images", i)
        i+=1

for images in image_path.iterdir():
    print(images)
    if images.is_file():
        image_file = Image.open(images)
        extracted_text = pytesseract.image_to_string(image_file)
        print(extracted_text)

        
