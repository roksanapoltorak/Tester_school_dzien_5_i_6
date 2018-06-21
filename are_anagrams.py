def are_anagrams(first, second):
    hist1 = {}
    hist2 = {}

    for char in first.lower():
        hist1[char] = hist1.get(char, 0) + 1


    for char in second.lower():
        hist2[char] = hist2.get(char, 0) + 1


    if hist1 == hist2:
        return True
    else:
        return False