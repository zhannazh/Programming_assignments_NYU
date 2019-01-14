""" This module handles the user's input of Year"""

import sys
import os
import pandas as pd
import numpy as np
from exceptions import *

def process_input(year):   
    
    """Handles the user's input of Year and raises exceptions when encountered"""
    # If no exceptions raised and input is not "finish," returns year as integer and prompts the main program to run Question 7
    # If input is "finish," returns "finish" that prompts the main program to run Question 8
    # If an exception is raised," returns False that prompts the main program to ask the user for another year or exits  
    
    while True:
        try:
   
            if year.lower() == 'quit' or year.lower() == 'exit':
                raise Quit    
            elif len(year) == 0:
                raise NoInput
            elif year.isdigit() is False and year.lower() != 'finish':
                raise ElementsOtherThanDigits
            elif len(year) >0 and year.isdigit() is True:
                if int(year) < 1800 or int(year)>2012:
                    raise OutofRange
            elif year.lower() == 'finish':
                return 'finish'
            
        except NoInput:
            print("No input. Try again.")
            return False
            break
        except ElementsOtherThanDigits:
            print("Not numeric entry or negative. Try again.")
            return False
            break
        except OutofRange:
            print("Year is out of range. Try again.")
            return False
            break
        except Quit:
            print("END")
            sys.exit()
        except (KeyboardInterrupt, SystemExit):
            print("END")
            os._exit(1)
        
        else: 
            return int(year)

    