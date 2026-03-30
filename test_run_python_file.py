from functions.run_python_file import run_python_file

print("Running 'main.py'")
run_python_file("calculator", "main.py")

print("Running 'main.py'")
run_python_file("calculator", "main.py", ["3 + 5"])

print("Running 'tests.py'")
run_python_file("calculator", "tests.py")

print("Running '../main.py'")
run_python_file("calculator", "../main.py")

print("Running 'nonexistent.py'")
run_python_file("calculator", "nonexistent.py")

print("Running 'lorem.txt'")
run_python_file("calculator", "lorem.txt")