import os
from log_handling import get_logger

log = get_logger()
match_case = False

# Accepted file type array
accepted_file = [".epub", ".mobi", ".pdf", ".txt"]

# Define the file path TODO: take user file input
file_path = r""

# Check if the file exists
if not os.path.exists(file_path):
    log.error(f"FileNotFoundError: The specified file '{file_path}' does not exist.")
    raise FileNotFoundError("The specified file does not exist.")

# Unpacking the tuple 
file_name, file_type = os.path.splitext(file_path)

try:
    log.info(f"Checking file type for: '{file_name}' with extension '{file_type}'")
    
    # Check if the file type is in the accepted list (case-sensitive)
    if file_type in accepted_file:
        match_case = True
        log.info(f"File type '{file_type}' is supported.")
    else:
        log.warning(f"File type '{file_type}' is not supported. Raising ValueError.")
        raise ValueError(f"{file_type} is not supported.")
except ValueError as e:
    log.error(f"ValueError: {e}")  # Log the ValueError with the message
except Exception as e:
    log.error(f"An unexpected error occurred: {e}")  # Log any other unexpected exceptions
finally:
    log.info("File type check complete.")
    log.info(f"Match case: {match_case}")