import string

def pangram(text):

    letters = string.ascii_lowercase
    text=text.lower()

    for i in letters:
        if i not in text:
            return False

    return True

def is_pangram2(text):
    found_letters = {}
    for char in text.lower():
        if char.isalpha():
            found_letters[char] = 0

    if len(found_letters) == len(string.ascii_lowercase):
        return True
    return False