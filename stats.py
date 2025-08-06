def get_book_text(filepath):
    with open(filepath) as f:
        return f.read()

def get_num_words(filepath):
    return len(get_book_text(filepath).split())

def get_num_chars(filepath):
    chars ={}
    for char in get_book_text(filepath):
        if char.lower() in chars:
            chars[char.lower()] += 1
        else:
            chars[char.lower()] = 1
    return chars