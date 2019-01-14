""" This module contains the main program that produces output as specified in assignment 9"""

# Author: Zhanna Zhanabekova (Net ID: zvz201)
# Date: December 3, 2016
# See readme.txt for a brief program description

# Import useful packages
import sys
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pylab
import seaborn as sns
from data_analysis import *
from exceptions import *
import process_input as inp
import change_country_name as change

# Question 1:
def load_countries(data):
        return pd.read_csv(data, header = 0, sep = ',')
countries = load_countries('countries.csv')
print("Q1: Dataset 'countries' loaded")

# Question 2:
def load_income(data,sheetname,column_index):
        return pd.read_excel(data,sheetname=sheetname,header=0, index_col=column_index)
income = load_income('indicator gapminder gdp_per_capita_ppp.xlsx', 'Data','gdp pc test')
print("Q2: Dataset 'income' loaded")
    
# Question 3:
income_transformed = income.transpose()
print("Q3: Print head of transformed 'income' dataset \n", income_transformed.head())

# Question 4:
def barh(year):
    """Plots income of each country (in a particular year) in a horizontal bar plot"""

    data_to_display = income_transformed.ix[year].dropna().sort_values(ascending=True)
    Title = "Distribution of Per Capita Income. All countries in " + str(year) + ". \n \n"
    ax = data_to_display.plot.barh(title = Title, width = 1.2, color ='r', figsize = (10,80), fontsize = 4)
    ax.set_xlabel("Income per capita")
    ax.set_ylabel("Countries")
    ax.xaxis.set_label_position('top')
    ax.xaxis.set_ticks_position('top')
    pylab.show()

# Question 5:
def merge_by_year(year):
    """Merges 'countries' with 'income' using 'Country' as key """
    """This is an inner join because we cannot use un-matched countries in plots """

    income_data = pd.DataFrame(income[year])
    income_data = income_data.rename(columns = {year:'Income'})
    
    # ! Important! 
    # I notice that sometimes country names differ in the two datatest and hence change 14 names in 'countries' data to ensure a match. See change_country_name.py for more information. Inner join n goes up from 177 to 191.
    countries_renamed = change.change_name(countries)
    
    # Country is a column in 'countries_renamed' but index in income_data
    merged_data =pd.merge(countries_renamed, income_data, left_on = 'Country',right_index=True)
    return merged_data


# Question 6
def main_program(year):
    """ Executes exploratory data analysis using data_analysis class"""
    data = merge_by_year(year)
    
    # Two types of histograms and one type of a boxplot grap are created 
    data_analysis(data,year).histogram_type1()
    data_analysis(data,year).histogram_type2()
    data_analysis(data,year).boxplot()

    
# Questions 7 and 8
def graphing():
    """First, prompts the user to enter Year and displays the graph as in Question 4"""
    """Then, after the user inputs "finish," generates graphs as in Question 6 for 2007-2012"""
    
    print("*****Enter Year *****")
    try:
        input_year= str(input())
    except (KeyboardInterrupt, SystemExit, EOFError):
        print("END")
        os._exit(1)
        
    no_white_space = input_year.replace(" ", "")
    processed_year = inp.process_input(no_white_space)
    
    if processed_year is not False and processed_year is not 'finish':
        # Generates graph as in Question 4. Repeats until gets "finish" input
        barh(processed_year)
    
    elif processed_year is 'finish':
        # Generates graphs as in Question 6, then ends the program
        for year in range(2007,2013):
            main_program(year)
        print('END')
        raise Quit
    
    else:
        return False #so that the user is prompted to enter input again
        


if __name__ == "__main__":
    while True:
        try:
            graphing()
    
        except (KeyboardInterrupt, SystemExit,Quit):
            os._exit(1)
