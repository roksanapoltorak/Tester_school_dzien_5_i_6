numbers = '123,25,256,5454'

def split(text, sep):
    parts = []
    current_part = []
    for char in text:
        if char != sep:
            current_part.append(char)
        else:
            parts.append(''.join(current_part))
            current_part = []
    parts.append(''.join(current_part))
    return parts