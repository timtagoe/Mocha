import os
from log_handling import get_logger

log = get_logger()
directory_name = 'Mocha'

def create_tmp_directory():
    temp_dir = os.path.join(os.getenv('TEMP', ''), directory_name)
    
    if not temp_dir:
        log.error("TEMP environment variable is not set.")
        return

    try:
        if not os.path.exists(temp_dir):
            os.makedirs(temp_dir)
            log.info(f"Temporary directory '{temp_dir}' created.")
        else:
            log.info(f"Temporary directory '{temp_dir}' already exists.")
    except Exception as e:
        log.error(f"An error occurred while creating the directory: {e}")

def create_tmp_path_file():
    temp_dir = os.path.join(os.getenv('TEMP', ''), directory_name)
    
    if not temp_dir:
        log.error("TEMP environment variable is not set.")
        return

    os.makedirs(temp_dir, exist_ok=True)
    temp_file_path = os.path.join(temp_dir, 'path_to_file.tmp')

    try:
        if not os.path.exists(temp_file_path):
            with open(temp_file_path, 'w') as f: 
                pass
            log.info(f'Temporary file created at: {temp_file_path}')
        else:
            log.info(f'The file {temp_file_path} already exists.')
    except Exception as e:
        log.error(f'An error occurred: {e}')

create_tmp_directory()
create_tmp_path_file()