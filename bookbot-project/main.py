def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)
    list_chars_sorted = get_list_chars_sorted(chars_dict)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document\n")
    
    for c in list_chars_sorted:
        if not c['char'].isalpha():
            continue
        print(f"The {c['char']} character was found {c['num']} times")

def sort_on(dict):
    return dict["num"]

def get_list_chars_sorted(chars_dict):
    list_chars_sorted = []
    for char in chars_dict:
        list_chars_sorted.append({"char": char, "num": chars_dict[char]})
    list_chars_sorted.sort(reverse=True, key=sort_on)
    return list_chars_sorted


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()

main()