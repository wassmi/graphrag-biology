import os
from langchain_community.document_loaders import PyPDFLoader

# Directory containing PDF files
pdf_directory = './pdf'

# Output directory for extracted text
output_directory = 'extracted_texts'

# Create output directory if it doesn't exist
os.makedirs(output_directory, exist_ok=True)

# Get a list of all PDF files in the directory
pdf_files = [f for f in os.listdir(pdf_directory) if f.endswith('.pdf')]

# Iterate through each PDF file and load it
for pdf_file in pdf_files:
    file_path = os.path.join(pdf_directory, pdf_file)
    print(f"Processing file: {file_path}\n")

    # Load the PDF and split it into pages
    loader = PyPDFLoader(file_path=file_path)
    pages = loader.load()

    # Extract text from pages
    text = '\n'.join([page.page_content for page in pages])

    # Remove .pdf extension from filename
    text_filename = pdf_file.replace('.pdf', '.txt')
    text_file_path = os.path.join(output_directory, text_filename)

    # Save extracted text to file
    with open(text_file_path, 'w') as f:
        f.write(text)

    print(f"Extracted text saved to {text_file_path}\n")