numbers = '123,25,256,5454'

def split2(text,sep):
    start = 0
    list = []

    for current, char in enumerate(text):
        if char == sep:
            list.append(text[start:current])
            start = current+1
    list.append(text[start:])

    return list