from data import DICTIONARY, LETTER_SCORES


def load_words():
    """Load dictionary into a list and return list"""
    with open(DICTIONARY, 'r') as file:
        return [word.rstrip('\n') for word in file]


def calc_word_value(word):
    """Calculate the value of the word entered into function
    using imported constant mapping LETTER_SCORES"""
    return sum(LETTER_SCORES.get(char.upper(), 0) for char in word.upper())


def max_word_value(words=DICTIONARY):
    """Calculate the word with the max value, can receive a list
    of words as arg, if none provided uses default DICTIONARY"""
    if words == DICTIONARY:
        words = load_words()
    max_value = 0
    max_word = None
    for word in words:
        word_value = calc_word_value(word)
        if word_value > max_value:
            max_value = word_value
            max_word = word
    return max_word


if __name__ == "__main__":
    pass # run unittests to validate
