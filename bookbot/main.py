from stats import num_words

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main():
    text = get_book_text("books/frankenstein.txt")
    count = num_words(text)
    print(f"Found {count} total words")
    
if __name__ == "__main__":
    main()
