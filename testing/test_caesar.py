from caesar import cipher
import pytest


def test_single_character():
    """Works with single characters, upper and lower case"""
    assert cipher("a", 5) == "f"
    assert cipher("A", 5) == "F"


def test_word():
    """Works on words with upper and lower case letters"""
    assert cipher("Hello", 5) == "Mjqqt"


def test_sentence():
    """Works on a full sentence"""
    assert cipher("What a string!", 5) == "Bmfy f xywnsl!"


def test_reverse():
    """Works with a negative index (to reverse a cipher)"""
    assert cipher("Bmfy f xywnsl!", -5) == "What a string!"


def test_wraps():
    """Shift rolls letters over correctly"""
    assert cipher("Z", 1) == "A"


def test_negative_wraps():
    """Shift rolls over correctly with negative shift"""
    assert cipher("A", -1) == "Z"


def test_large_factor():
    """Works with large shift factors"""
    assert cipher("What a string!", 75) == "Texq x pqofkd!"


def test_large_negative_factor():
    """Works with large negative shifts"""
    assert cipher("Texq x pqofkd!", -75) == "What a string!"
