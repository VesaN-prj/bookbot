from stats import get_num_words, get_sort_chars

def main():
    book = "books/frankenstein.txt"

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {get_num_words(book)} total words")
    print("--------- Character Count -------")
    for list_item in get_sort_chars(book):
        if list_item["char"].isalpha() == True:
            print(f"{list_item["char"]}: {list_item["num"]}")
    print("============= END ===============")

main()