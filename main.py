from stats import get_num_words, get_num_characters, sort_dict
import sys
if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
def main():
    path = sys.argv[1]

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")

    text = get_book_text(path)

    print("----------- Word Count ----------")
    total_words = get_num_words(text)
    print(f"Found {total_words} total words")

    print("--------- Character Count -------")
    chars_sorted = sort_dict(get_num_characters(text))
    for entry in chars_sorted:
        ch = entry["char"]
        if ch.isalpha(): 
            print(f"{ch}: {entry['num']}")

    print("============= END ===============")
main()
