def get_num_words(text):
    table = text.split()
    return len(table)

def get_num_char(text):
    text = text.lower()
    char_dict = {}
    for char in text:
        if char not in char_dict:
            char_dict[char] = 1
        else:
            char_dict[char] += 1
    return char_dict;

def sort_on(items):
    return items["num"]

def get_char_sorted(items):
    char_list = []
    for item in items:
        char_list.append({"char": item, "num": items[item]})
#    print(char_list)
#    print(char_list[2])
    char_list.sort(reverse=True, key=sort_on)
    return char_list
