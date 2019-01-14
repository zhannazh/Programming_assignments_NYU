""" This module processes inputs, handles errors, and calls the investment_instrument class to produce daily returns, histograms, and statistics"""

# Author: Zhanna Zhanabekova (Net ID: zvz201)
# Date:  November 27, 2016

# See readme.txt for a brief program description:

# import useful packages
import sys
import os
import numpy as np
import re
import matplotlib.pyplot as plt
from investment_instrument import *
from exceptions import *

#At the beginning of the program, specify what constitutes a valid input
print()
print("Instructions on how to enter positions:")
print("Only 1,10, 100, and 1000 are valid for a position entry.")
print("You are allowed to compare more than 1 position, i.e., 1 vs 100 vs 1000.")
print()


def user_entered_positions():
    """Function handles the user's input of investment positions, including raising exceptions"""
    while True:
        try:
            print("*****PLEASE ENTER A LIST OF POSITIONS, SEPARATED BY COMMAS, NO BRACKETS *****")
            input_number_of_shares = str(input())
        
            # Clean the positions input and check for basic mistakes
            no_white_space = input_number_of_shares.replace(" ", "")
            no_commas = no_white_space.replace(",", "")
            no_dots = no_commas.replace("\.", "")
        
            two_consecutive_commas = re.findall(',,', no_white_space)
            contains_dots = re.findall("\.", input_number_of_shares)     
        
            split_input = no_white_space.split(',')
            numbers_in_input = []
            for i in split_input:
                numbers_in_input.append(i)
        
            #positions_input will be used as an input in investment_instrument.py (define it outside too)
            positions_input = []
              
            if input_number_of_shares.lower() == 'quit' or input_number_of_shares.lower() == 'exit':
                raise Quit
            elif len(input_number_of_shares) == 0:
                raise NoInput
            elif len(two_consecutive_commas) > 0:
                raise TWoconsecutiveCommas
            elif len(contains_dots) > 0:
                raise ContainsPeriod
            elif no_dots.isdigit() is False and input_number_of_shares.lower() != 'quit' and input_number_of_shares.lower() != 'exit':
                raise ElementsOtherThanDigits
            elif no_white_space[-1] == ",":
                raise LastElementIsComma
            elif len(numbers_in_input)>0:
                for i in numbers_in_input:
                    if int(i)!=1 and int(i)!=10 and int(i) != 100 and int(i) !=1000:
                        raise NotCorrectInput
                    else:
                        positions_input.append(int(i))
            return positions_input
            break        

        except NoInput:
            print("WARNING: THE INPUT IS EMPTY. PLEASE TRY AGAIN.")
            print()
        except TWoconsecutiveCommas:
            print("WARNING: THE INPUT CONTAINS AT LEAST 2 CONSECUTIVE COMMAS. PLEASE TRY AGAIN.")
            print()
        except ContainsPeriod:
            print("WARNING: THE INPUT CONTAINS PERIODS OR DECIMAL POINTS. PLEASE TRY AGAIN.")
            print()
        except ElementsOtherThanDigits:
            print("WARNING: THE INPUT CONTAINS ELEMENTS OTHER THAN DIGITS (EX: LETTERS, #,-}). PLEASE TRY AGAIN.")
            print()
        except LastElementIsComma:
            print("WARNING: THE LAST ELEMENT OF THE INPUT IS A COMMA. PLEASE TRY AGAIN.")
            print()
        except NotCorrectInput:
            print("WARNING: ONLY 1, 10, 100, and 1000 ARE VALID POSITION INPUTS. PLEASE TRY AGAIN.")
            print()
        except Quit:
            print("END")
            sys.exit()
        except (KeyboardInterrupt, SystemExit):
            print("END")
            os._exit(1)

def user_entered_simulations():
    """Function handles user-specified number of simulations """
    while True:
        try:
            print("*****PLEASE ENTER THE NUMBER OF SIMULATIONS TO BE RUN*****")
            input_number_of_simulations = str(input()).replace(" ", "")
             
            if input_number_of_simulations.lower() == 'quit' or input_number_of_simulations.lower() == 'exit':
                raise Quit
            elif len(input_number_of_simulations) == 0:
                raise NoInput 
            elif input_number_of_simulations.isdigit() is False and input_number_of_simulations.lower() != 'quit' and input_number_of_simulations.lower() != 'exit':
                raise ElementsOtherThanDigits
            elif len(input_number_of_simulations) >0:
                number_of_simulations = int(input_number_of_simulations)
            return number_of_simulations
            break

        except NoInput:
            print("WARNING: THE INPUT IS EMPTY. PLEASE TRY AGAIN.")
            print()
        except ElementsOtherThanDigits:
            print("INPUT FOR THE NUMBER OF SIMULATIONS IS NOT A VALID INTEGER NUMBER OR CONTAINS COMMAS. PLEASE TRY AGAIN.")
            print()
        except Quit:
            print("END")
            sys.exit()
        except (KeyboardInterrupt, SystemExit):
            print("END")
            os._exit(1)

positions_input = user_entered_positions()  
number_of_simulations = user_entered_simulations()

def main_program(positions_input, number_of_simulations):
    """This is the main program that takes the clean inputs and calls the investment_instrument class.
    The program iterates through each investment position and outputs a histogram and mean/std stats. 
    """
    print("Please WAIT! The program is calculating daily returns for your inputted scenarios. This may take a while.")
    
    # this is the file where the stats results will be saved
    file = open("results.txt", "w")
    file.close()
    for i in positions_input:
        # for each position, define daily_return using the class to "fix" simulated results so that
        # the histogram and stats are produced using the same daily return values
        daily_ret = investment_instrument(i,number_of_simulations).generate_daily_returns()
        investment_instrument(i,number_of_simulations).histogram(daily_ret)
        investment_instrument(i,number_of_simulations).summary_stats(daily_ret)        

# Run the main_program when executing assignment8.py        
if __name__ == "__main__":
    try:
        main_program(positions_input, number_of_simulations)
        print()        
        print("Please CHECK YOUR FOLDER for histograms saved as pdf files and results.txt file.")
        
    except (KeyboardInterrupt, SystemExit):
        print("End by KeyboardInterrupt or SystemExit")
        print()

      
    