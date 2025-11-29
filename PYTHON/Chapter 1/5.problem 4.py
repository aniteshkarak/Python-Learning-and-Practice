import os

def print_directory_contents(path='.'):
    try:
        entries = os.listdir(path)
        print(f"Contents of directory '{path}':")
        for entry in entries:
            print(entry)
    except FileNotFoundError:
        print(f"The directory '{path}' does not exist.")
    except NotADirectoryError:
        print(f"'{path}' is not a directory.")
    except PermissionError:
        print(f"Permission denied when accessing '{path}'.")
    except OSError as e:
        print(f"Error accessing '{path}': {e}")

if __name__ == '__main__':
    # you can replace '.' with any directory path
    print_directory_contents('.')
