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

def dict_to_list(dictionary):
    report_list = []
    for key in dictionary:
        num = dictionary[key]
        loop_dict = {
            "char" : key,
            "num" : num,
        }
        report_list.append(loop_dict)
    report_list.sort(reverse=True, key=sort_on)
    return report_list

def sort_on(dict_list):
    return dict_list["num"]
    