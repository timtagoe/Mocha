from file_handling.log_handling import setup_logging
from file_handling.tmp_handling import create_tmp_directory, create_tmp_path_file

def main():
    # Set up logging
    setup_logging()
    
    create_tmp_directory()
    create_tmp_path_file()

if __name__ == "__main__":
    main()
