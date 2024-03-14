import openai
import pytesseract
import os
import matplotlib.pyplot as plt
from PIL import Image
from io import BytesIO
import fitz
import anthropic

client = anthropic.Anthropic(
    api_key="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"
)

openai.api_key = "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"

data_string1 str ="This is the name"


def document_to_string(document_path, list_dict_final_images=None):
    # Check the file extension to determine the type of document
    _, file_extension = os.path.splitext(document_path)

    if file_extension.lower() in ['.png', '.jpeg', '.jpg']:
        # Load the image for PNG, JPEG, JPG files
        image = Image.open(document_path)
        # Perform OCR on the image to extract text
        list_final_images = pytesseract.image_to_string(image)
        return list_final_images

    all_images = [list(data.values())[0] for data in list_dict_final_images]

    for index, image_bytes in enumerate(all_images):
        image = Image.open(BytesIO(image_bytes))
        figure = plt.figure(figsize=(image.width / 100, image.height / 100))

        plt.title(f"--- Page Number {index + 1} ---")
        plt.imshow(image)
        plt.axis("off")
        plt.show()


# -------------------------------------------------------------------------------
# Below is the PDF to Image
def pdf_to_image(file_path, scale=300 / 72):
    text = ""
    pdf_document = fitz.open(file_path)

    for page_num in range(pdf_document.page_count):
        page = pdf_document.load_page(page_num)
        text += page.get_text()

    pdf_document.close()
    return text


# -------------------------------------------------------------------------------


def convert_any_to_string(filepath):
    my_path = filepath
    if my_path.endswith(".pdf"):
        return pdf_to_image(my_path)

    elif my_path.endswith(".png"):
        return document_to_string(my_path)

    elif my_path.endswith(".jpeg"):
        return document_to_string(my_path)

    elif my_path.endswith(".jpg"):
        return document_to_string(my_path)

    else:
        return "The extension is not valid!"


def main():
    global text
    global data_string
    filepath = "sample-invoice.pdf"
    new_path = filepath.lower()

    try:
        text = convert_any_to_string(new_path)
    # print("Document content as string: \n ", text)
    except Exception as e:
        print("Error: ", e)

    data_string = text
    data_string1 = data_string
    #print(data_string)

print(data_string1)



if __name__ == "__main__":
    main()
