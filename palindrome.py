def is_palindrome(text):
    """
    Checks if text is a palindrome.
    Args:
        text: string to be checked
    Returns:
        True if text is a palindrome, False otherwise.
    """
    text = text.lower()
    word = ''
    l = len(text) - 1

    while l >= 0:
        word = word + text[l]
        l -= 1

    if word == text:
        return True
    else:
        return False

def palindrome(text):
    text = text.lower()
    for i in range(len(text) // 2):
        if text[i] != text[len(text) - i - 1]:
            return False
    return True