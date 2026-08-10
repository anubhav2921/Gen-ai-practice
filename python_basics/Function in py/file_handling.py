#File handling in python 

# File handling: reading, writing, and appending 

# Common File Modes
# Mode	Description
# "r"	Read (default)
# "w"	Write (creates a new file or overwrites existing)
# "a"	Append (adds data to the end)
# "x"	Create a new file (fails if file exists)
# "b"	Binary mode
# "t"	Text mode (default)
# "+"	Read and write

from pathlib import Path

file_path = Path(__file__).with_name("data.txt")

with open(file_path, "r", encoding="utf-8") as f:
    print(f.read())
