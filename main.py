from stats import get_num_words, get_num_chars, get_sort_chars
import sys


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    num_chars = get_num_chars(text)
    sort_chars = get_sort_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sort_chars:
        if item["char"].isalpha():
            print(f"{item["char"]}: {item["count"]}")
    print("============= END ===============")



def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()


main()
