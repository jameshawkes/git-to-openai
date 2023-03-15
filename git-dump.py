import os
import sys
import pyperclip

def is_python_or_cpp(file):
    _, ext = os.path.splitext(file)
    return ext in ('.py', '.cpp', '.hpp', '.h', '.cc', '.cxx', '.c')

def read_files(startpath):
    file_contents = []
    for root, _, files in os.walk(startpath):
        for f in files:
            if is_python_or_cpp(f):
                filepath = os.path.join(root, f)
                try:
                    with open(filepath, 'r') as file:
                        content = file.read()
                        file_contents.append((filepath, content))
                except Exception as e:
                    print(f"Error reading file {filepath}: {e}")

    return file_contents

def chunks(lines, n):
    for i in range(0, len(lines), n):
        yield lines[i:i + n]

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python git-dump.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]
    all_contents = read_files(directory)
    all_lines = []

    for filepath, content in all_contents:
        all_lines.append(f"=== {filepath} ===\n{content}")

    all_lines = "\n".join(all_lines).splitlines()

    for i, chunk in enumerate(chunks(all_lines, 300)):
        chunk_text = f"=== Chunk {i + 1} ===\nRead this, say OK when you are done.\n" + "\n".join(chunk)
        pyperclip.copy(chunk_text)
        print(f"Copied chunk {i + 1} to clipboard. Press Enter to continue...")
        input()