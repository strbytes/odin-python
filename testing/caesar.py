from string import ascii_lowercase as lowers
from string import ascii_uppercase as uppers


def cipher(string, shift):
    """Return a version of string encrypted with Caesar's cipher, using the
    supplied shift"""
    result = ""
    # for each char in string, if a letter then apply the cipher
    for char in string:
        if char in lowers:
            i = lowers.index(char)
            # adjust for large ciphers
            i += shift
            i %= 26
            result += lowers[i]
        elif char in uppers:
            i = uppers.index(char)
            # adjust for large ciphers
            i += shift
            i %= 26
            result += uppers[i]
        else:
            result += char
    return result
