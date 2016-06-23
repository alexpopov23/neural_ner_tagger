import string

def get_case_vector (word):

    if word.istitle():
        return [1.0, 0.0, 0.0, 0.0]
    if word.isupper():
        return [0.0, 1.0, 0.0, 0.0]
    if word.islower():
        return [0.0, 0.0, 1.0, 0.0]
    if word in string.punctuation:
        return [0.0, 0.0, 0.0, 1.0]
    return [0.0, 0.0, 0.0, 0.0]

def get_suffix (word):

    title, isAllCaps, isLower, isDigit = False, False, False, False
    if word.istitle():
        title = True
    if word.isupper():
        isAllCaps = True
    if word.islower():
        isLower = True
    if word.isdigit():
        isDigit = True

    if isDigit:
        word = len(word)*"0"
        return word
    if len(word) > 3:
        word = word[-3:]
        word = "_" + word
    if len(word) > 1 and isAllCaps:
        word = "$" + word
    if title:
        word = "@" + word
    if not (title or isLower or isAllCaps or word in string.punctuation):
        word = "#" + word
    return word.lower()

