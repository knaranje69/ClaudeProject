import os
from claude3.sonnet import Claude3Sonnet
import anthropic

# Initialize the Claude3Sonnet object
claude = Claude3Sonnet()

# Prompt the user for the file path
file_path = input("Enter the file path: ")

# Check if the file exists
if os.path.isfile(file_path):
    # Load the document
    with open(file_path, 'r') as file:
        document = file.read()

    # Prompt the user for the extraction method
    extraction_method = input("Enter the extraction method (sentence, paragraph, or full): ")

    # Extract text from the document based on the user's input
    if extraction_method.lower() == 'sentence':
        extracted_text = claude.extract_sentences(document)
    elif extraction_method.lower() == 'paragraph':
        extracted_text = claude.extract_paragraphs(document)
    elif extraction_method.lower() == 'full':
        extracted_text = document
    else:
        print("Invalid extraction method. Please try again.")
        exit()

    # Print the extracted text
    print("\nExtracted Text:\n")
    for text in extracted_text:
        print(text)
        print()

else:
    print("The file path is invalid. Please try again.")