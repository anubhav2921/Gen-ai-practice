import os

given_path = r"C:\practice-gen-ai\python_basics\intro.ipynb"

if os.path.exists(given_path):
    print("yes")
else:
    print("no")