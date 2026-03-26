import os
from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))
        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            print(f'Error: Cannot read "{file_path} as it is outside the permitted working directory')
            return
        
        if not os.path.isfile(target_file) or os.path.islink(target_file):
            print(f'Error: File not found or is not a regular file: "{file_path}"')
            return

        with open(target_file, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if f.read(1):
                file_content_string += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
        print(file_content_string)
    except ValueError:
        print("Error: paths are both absolute and relative, on a different drive or empty")
    except OSError:
        print("Error: file does not exist or inaccessible")
    except TypeError:
        print("Error: non-string values in iterable")
    except:
        print("Error: some error occured")