import os

def get_files_info(working_directory, directory="."):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))
        valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

        if not valid_target_dir:
            print(f'Error: Cannot list "{directory} as it is outside the permitted working directory')
            return
        
        if not os.path.isdir(target_dir) or os.path.islink(target_dir):
            print(f'Error: "{directory}" is not a directory')
            return

        dir_content = os.listdir(target_dir)
        target_dir_contents = ""

        for item in dir_content:
            file_path = os.path.join(target_dir, item)
            print(f"- {item}: file_size={os.path.getsize(file_path)}, is_dir={os.path.isdir(file_path)}")
    except ValueError:
        print("Error: paths are both absolute and relative, on a different drive or empty")
    except OSError:
        print("Error: file does not exist or inaccessible")
    except TypeError:
        print("Error: non-string values in iterable")
    except:
        print("Error: some error occured")