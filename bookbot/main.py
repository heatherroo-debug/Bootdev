from stats import num_words, char_count

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    word_count = num_words(text)
    character_count = char_count(text)
    print(f"Found {word_count} total words")
    print(f"character couunt is {character_count}")


if __name__ == "__main__":
    main()
