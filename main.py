from stats import *
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
        return file_contents

def main():
    path = sys.argv[1]
    num_words = get_num_words(get_book_text(path))
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    character_count = count_characters(get_book_text(path))
    list_of_sorted_char = dict_to_list(character_count)
    for item in list_of_sorted_char:
        if item["char"].isalpha():
            print(item["char"], ": ", item["count"], sep="")

if (len(sys.argv) != 2):
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()