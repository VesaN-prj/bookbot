from stats import get_num_words, get_num_chars

def main():
    book = "./books/frankenstein.txt"
    
    print(f"{get_num_words(book)} words found in the document")
    print(get_num_chars(book))

main()