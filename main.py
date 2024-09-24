def main():
    create_report()


def get_book_text(path):
    with open(path) as f:
        return f.read()
    
def get_word_count(text):
    words = text.split()
    return len(words)

def get_character_count(text):
    lower_text = text.lower()
    char_dict = {}
    for char in lower_text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict

def sort_on(dict):
    return dict['count']

def sort_chars(char_dict):
    dict_list = []
    for key in char_dict:
        if key.isalpha():
            dict_list.append({'char': key, 'count': char_dict[key]})
    dict_list.sort(key=sort_on, reverse=True)
    return dict_list

def create_report():
    book_path = 'books/frankenstein.txt'
    book_text = get_book_text(book_path)
    word_count = get_word_count(book_text)
    char_count = get_character_count(book_text)
    sorted_chars = sort_chars(char_count)
    print(f"-- Begin report of {word_count} --")
    print(f"The book contains {word_count} words")
    print("")
    for char in sorted_chars:
        print(f"The '{char['char']}' appears {char['count']} times")
    print("-- End of report --")

main()