import sys
from stats import get_num_words, get_chars_dict, get_sorted_dicts

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    print(f"Analyzing book found at {book_path}...")
    num_words = get_num_words(text)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    chars_dict = get_chars_dict(text)
    sorted_dicts = get_sorted_dicts(chars_dict)
    print("--------- Character Count -------")
    for dict in sorted_dicts:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")
    print("============= END ===============")

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()

main()