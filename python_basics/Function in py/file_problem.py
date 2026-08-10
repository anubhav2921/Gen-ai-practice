# Reading the total number of lines, words, and characters from a file.

from pathlib import Path


def file_problem(file):
    with open(file, 'r', encoding='utf-8') as files:
        lines = files.readlines()
        total_lines = len(lines)
        total_words = sum(len(line.split()) for line in lines)
        total_characters = sum(len(line) for line in lines)
        return total_lines, total_words, total_characters


base_dir = Path(__file__).resolve().parent
file_path = base_dir / 'Total_data.txt'

if not file_path.exists():
    fallback = base_dir / 'data.txt'
    if fallback.exists():
        file_path = fallback
    else:
        raise FileNotFoundError("Neither Total_data.txt nor data.txt exists in the same folder as this script.")


total_lines, total_words, total_characters = file_problem(file_path)

print(f"total lines are : {total_lines} and total words are : {total_words} and total characters are : {total_characters}")