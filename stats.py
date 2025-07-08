def word_count(text):
    word_list = text.split()
    return len(word_list)

def character_count(text):
    text = text.lower()
    letter_count = {}
    for char in text:
        letter_count[char] = letter_count.get(char,0)+1
    return letter_count

def sort_on(item):
    return item["num"]

def count_sort(letter_count):
    char_counts = []
    for item in letter_count:
        character_count = {"char" : item,"num":letter_count[item]}
        char_counts.append(character_count)
    char_counts.sort(reverse=True,key=sort_on)
    return char_counts
