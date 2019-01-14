""" This module contains user-defined exceptions"""
# All exceptions have to do with the user input (+KeyboardInterrupt or SystemExit)


class Error(Exception):
    """Base class for other exceptions"""
    pass

class ElementsOtherThanDigits(Error):
    """Raised when input contains elements other than digits"""
    pass

class OutofRange(Error):
    """Raised when the year input is out of range"""
    pass

class NoInput(Error):
    """Raised when (any) input is empty"""
    pass

class Quit(Error):
    """Quit the program"""
    pass

