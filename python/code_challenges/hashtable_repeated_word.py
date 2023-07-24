from data_structures.hashtable import Hashtable

def first_repeated_word(input_string):
    words = []
    word_count = {}
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    first_repeat = None
    for word in words:
        word = word.lower()
        if word_count[word] > 1:
            first_repeat = word
            break
    return first_repeat


__name__ == "__main__"
input_str = "This is a test string with repeated words like is and a."
first_repeated_word()
