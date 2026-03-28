import os

def write_file(working_directory, file_path, content):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Create parent directories if they don't exist
        parent_dir = os.path.dirname(target_file)
        if parent_dir:  # avoid error on empty dirname
            os.makedirs(parent_dir, exist_ok=True)

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            print(f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
            return

        if os.path.isdir(target_file):
            print(f'Error: Cannot write to "{file_path}" as it is a directory')
            return

        with open(target_file, "w") as f:
            result = f.write(content)
            if result:
                print(f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    except ValueError:
        print("Error: paths are both absolute and relative, on a different drive or empty")
    except OSError:
        print("Error: file does not exist or inaccessible")
    except TypeError:
        print("Error: non-string values in iterable")
    except:
        print("Error: some error occured")