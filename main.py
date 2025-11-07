from stats import get_num_words, get_char_sorted, get_num_char
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(sys.argv[1])
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(text)} total words")
#    print(f"{get_num_char(text)}")
    print("--------- Character Count -------")
    sorted_list = get_char_sorted(get_num_char(text))
    for char in sorted_list:
        if char['char'].isalpha():
            print(f"{char['char']}: {char['num']}")
    #print(f"{get_char_sorted(get_num_char(text))}")
    print("============= END ===============")

main()
