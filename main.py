from stats import character_count,word_count,count_sort
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    title = sys.argv[1]
    text = ""
    
    with open(title) as f:
        text = f.read()
        total_words = word_count(text)
        letter_count = character_count(text)
        sorted = count_sort(letter_count)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {title}...")
        print("----------- Word Count ----------")
        print(f"Found {total_words} total words")
        print("--------- Character Count -------")
        for char in sorted:
            if char["char"].isalpha():
                print(f"{char["char"]}: {char["num"]}")
        print("============= END ===============")
    

main()