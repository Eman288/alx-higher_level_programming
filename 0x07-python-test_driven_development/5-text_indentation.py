#!/usr/bin/python3
"""a function that do text indentation"""


def text_indentation(text):
    """a function that do text indentation

    text => the text to be printed
    """
    if isinstance(text, str) is not True:
        raise TypeError("text must be a string")
    j = 0
    for j in range(len(text)):
        if (text[j] != ' '):
            break
    for i in range(len(text)):
        if text[i] == '.' or text[i] == '?' or text[i] == ':':
            print("{}\n".format(text[j:i + 1]), end='\n')
            for k in range(i + 1, len(text)):
                if text[k] != ' ':
                    j = k
                    break
