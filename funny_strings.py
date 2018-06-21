"""
Module for funny string manipulations
"""

from random import randint

def randomize(text):
    """
    Returns randomized string.
    Args:
        text to randomized
    Returns:
        randomized text
    """

    word = []

    for idx, char in enumerate(text):
        if randint(0,1):
            word.append(char.upper())
        else:
            word.append(char.lower())
    return ''.join(word)



def numberize(text):
    word = ''

    for char in text.lower():
        if char == 'e':
            word += '3'
        elif char == 'o':
            word += '0'
        elif char == 'i':
            word += '!'
        elif char == 'a':
            word += '@'
        elif char == char:
            word += char

    return word


def bubbleize(text):
    """
    Returns bubbleized string.
    Args:
        text
    Returns:
        bubbleized text
    """

    word = []

    for idx, char in enumerate(text):
        if idx % 2:
            word.append(char.upper())
        else:
            word.append(char.lower())
    return ''.join(word)