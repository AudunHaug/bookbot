from stats import *

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = "books/frankenstein.txt"
    print(f"{get_num_words(get_book_text(path))} words found in the document")
    print(count_characters(get_book_text(path)))

main()