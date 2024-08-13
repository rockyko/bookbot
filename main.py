def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    
    numbers_dict = get_char_to_number_dict(text)
    reversed_list = reverse_dict(numbers_dict)
    print(f"--- Begin report of {book_path} ---")
    print(f"{num_words} words found in the document \n")
    print(print_dict_in_list(reversed_list))
    print("=== end ===")

def get_num_words(text):
    words = text.split()
    return len(words)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_char_to_number_dict(text):
    char_to_number_dict = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for char in text:
        lowered = char.lower()
        if lowered in char_to_number_dict:
            char_to_number_dict[lowered] += 1
    return char_to_number_dict  

def sort_on(d):
    return d["num"]

def reverse_dict(d):
    reversed_list = []
    for char in d:
        reversed_list.append({"char": char, "num": d[char]})       
    return sorted(reversed_list, reverse=True, key=sort_on)

def print_dict_in_list(l):
    for d in l:
        if d['char'].isalpha():
            print(f"The '{d['char']}' character was found {d['num']} times")



main()     

