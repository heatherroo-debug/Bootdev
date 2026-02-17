from stats import num_words, char_count, dict_to_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = num_words(text)
    char_dict = char_count(text)
    sorted_list = dict_to_list(char_dict)
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        character = item["char"]
        count = item["num"]
        if character.isalpha() == True:
            print(f"{character}: {count}")
    print("============= END ===============")



if __name__ == "__main__":
    main()
