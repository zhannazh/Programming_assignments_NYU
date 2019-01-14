""" This module contains user-defined exceptions"""
# All exceptions have to do with the user input (+KeyboardInterrupt or SystemExit)
# See comments below to get a sense of what errors & exceptions the program can handle

class Error(Exception):
    """Base class for other exceptions"""
    pass

class TWoconsecutiveCommas(Error):
    """Raised when the positions input contains at least 2 consecutive commas"""
    pass

class ContainsPeriod(Error):
    """Raised when (any) input contains dots/periods (e.g., a decimal number is entered)"""
    pass

class ElementsOtherThanDigits(Error):
    """Raised when (any) input contains elements other than digits (letters, #,},-, etc.)"""
    pass

class LastElementIsComma(Error):
    """Raised when the last element in the positions input is a comma"""
    pass

class NotCorrectInput(Error):
    """Raised when the element of the positions input is neither 1, nor 10, nor 100, nor 1000"""
    pass

class NoInput(Error):
    """Raised when (any) input is empty"""
    pass

class Quit(Error):
    """Quit the program"""
    pass

