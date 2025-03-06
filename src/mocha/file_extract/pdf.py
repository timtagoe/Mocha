import toml
import os
from pypdf import PdfReader

# Load the configuration from pyproject.toml
config = toml.load("pyproject.toml")
directory_name = config["tool"]["Mocha"]["temporary_directory"]
file_name = config["tool"]["Mocha"]["temporary_path_to_file"]

# Create the full path to the PDF file
path_to_file = os.path.join(os.getenv('TEMP'),directory_name, file_name)

# Read file contents 
path_to_file = open(path_to_file, "r")
content = path_to_file.read()

# Load the PDF file 
book = PdfReader(content)
# Initialize a list to hold the text content
text_content = []

# Iterate through each page in the PDF
for page in book.pages:
    # Extract text from the page and append it to the list
    text_content.append(page.extract_text())

# Optionally, join the list into a single string if needed
full_text = "\n".join(text_content)

# Print the extracted text (or do something else with it)
print(full_text)