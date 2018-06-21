import string

def count_chars(text):
    hist = {}

    for char in text:
        if char.isalpha():
            if char.islower():
                hist['lower'] = hist.get('lower', 0) + 1
            else:
                hist['upper'] = hist.get('upper', 0) + 1
        if char.isdigit():
            hist['digits'] = hist.get('digits', 0) + 1
    return hist