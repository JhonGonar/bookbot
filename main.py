from stats import get_num_words, get_book_text, count_chars, sort_by_count
import sys

def main():
    if len(sys.argv) != 2 :
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path_file = sys.argv[1]
    book_text = get_book_text(path_file)
    num_words = get_num_words(book_text)
    chars_counter = count_chars(book_text)
    sorted_counter = sort_by_count(chars_counter)
    print(f"============ BOOKBOT ============")
    print(f"Analyzing book found at {path_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for i in sorted_counter:
        if i["character"].isalpha():
            print(f"{i["character"]}: {i["count"]}")
    print("============= END ===============")
main()