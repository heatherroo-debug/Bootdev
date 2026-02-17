def num_words(text):
    word_list = text.split()
    word_count = len(word_list)
    return word_count

def char_count(text):
    char_dict = {}
    lower_text = text.lower()
    for character in lower_text:
        if character not in char_dict:
            char_dict[character] = 1
        else:
            char_dict[character] += 1
    return char_dict

def sort(char_dict):
    sorted_dict = char_dict.sort()
    print(f"sorted dictionary is {sorted_dict}")
    return sorted_dict