import os, subprocess

def run_python_file(working_directory, file_path, args=None):
    try:
        working_dir_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_dir_abs, file_path))

        # Create parent directories if they don't exist
        # parent_dir = os.path.dirname(target_file)
        # if parent_dir:  # avoid error on empty dirname
        #     os.makedirs(parent_dir, exist_ok=True)

        valid_target_file = os.path.commonpath([working_dir_abs, target_file]) == working_dir_abs

        if not valid_target_file:
            print(f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')
            return

        if not os.path.isfile(target_file):
            print(f'Error: "{file_path}" does not exist or is not a regular file')
            return

        if not target_file.endswith('.py'):
            print(f'Error: "{file_path}" is not a Python file')
            return

        command = ["python", target_file]

        if args:
            command.extend(args)
        
        completed_process = subprocess.run(
            command, 
            cwd=working_dir_abs,
            timeout=30,
            capture_output=True, 
            text=True
        )
        output_string = ""
        out_capture = completed_process.stdout
        err_capture = completed_process.stderr
        return_code = completed_process.returncode

        if return_code != 0:
            output_string += f"Process exited with code {return_code}\n"
        if (out_capture is None or out_capture == "") and (err_capture is None or err_capture == ""):
            output_string += f"No output produced\n"
        else: 
            output_string += f"STDOUT: {out_capture}\n"
            output_string += f"STDERR: {err_capture}\n"

        print(output_string)

    except Exception as e:
        print(f"Error: executing Python file: {e}")