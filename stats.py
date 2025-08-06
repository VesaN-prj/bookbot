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

def get_sort_chars(filepath):
    list_a = []
    for char, num in get_num_chars(filepath).items():
        dict_a = {"char": char, "num": num}
        list_a.append(dict_a)
    list_a.sort(key=lambda d: d["num"], reverse=True)
    # sorted_list_a = sorted(list_a, key=lambda d: d["num"], reverse=reversed)
    return list_a
