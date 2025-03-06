import ebooklib
from ebooklib import epub
from bs4 import BeautifulSoup

# Load the EPUB file
book = epub.read_epub(r"C:\Users\Tim\Downloads\wells-sleeper-awakes.epub")
# Initialize a list to hold the text content
text_content = []

# Iterate through the items in the EPUB file
for item in book.get_items():
    # Check if the item is of type 'EpubHtml'
    if item.get_type() == ebooklib.ITEM_DOCUMENT:
        # Use BeautifulSoup to parse the HTML content
        soup = BeautifulSoup(item.get_body_content(), 'html.parser')
        # Extract text and append to the list
        text_content.append(soup.get_text())

# Join all text content into a single string
full_text = "\n".join(text_content)

# Print or process the extracted text
print(full_text)