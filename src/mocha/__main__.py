from log_handling import setup_logging
from tmp_handling import create_tmp_directory, create_tmp_path_file

def main():
    # Set up logging
    setup_logging()

    # Now you can call your functions
    create_tmp_directory()
    create_tmp_path_file()

if __name__ == "__main__":
    main()