import os.path


def main():
    read_file("file.txt")
    write_text_to_file("result.txt", text)
    rewrite("result.txt")


def read_file(fname):
    try:
        file = open(fname, 'r', encoding='utf-8')
        print('File ' + fname + ':')
        for line in file:
            print(line, end='')
        file.close()
    except FileNotFoundError:
        print("Файл не знайдено: " + fname)


text = '''Hello!
I am a text file. And I had been written with a Python script
before you opened me, so look up the docs and try to delete
me using Python, too.'''


def write_text_to_file(filename, text):
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f"\nFile {filename} written successfully!")


def rewrite(fname):
    filename = os.path.join(fname)
    with open(filename, 'r') as file:
        lines = file.readlines()
    lines.insert(2, 'inserted line\n')
    with open(filename, 'w') as file:
        file.writelines(lines)
    print(f"File {fname} rewritten successfully!")

if __name__ == '__main__':
    main()
