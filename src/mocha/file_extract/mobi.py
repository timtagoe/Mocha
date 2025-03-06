import mobi

# Convert MOBI to text
mobi_file = mobi.Mobi()
mobi_file.parse()
text = mobi_file.get_text()

print(text)

