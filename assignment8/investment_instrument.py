""" This module contains class investment_instrument that generates daily returns for each position, produces a histogram (in a pdf file), and saves the mean and std of daily returns for each position in results.txt file."""

import sys
import os
import numpy as np
import re
from random import randint
import matplotlib.pyplot as plt

class investment_instrument:
    
    # Note that all exceptions are handled in module assignment8.py      
    
    def __init__(self, position, num_trials):
        """Initiate an instance of the investment_instrument class. A function of an investment position"""

        self.position = position        
        self.num_trials = num_trials
        self.position_value = np.true_divide(1000, self.position) 
        
        # this will be used in the histogram text and results.txt  
        if self.position == 1:
            self.position_word = " position "
        else:
            self.position_word = " positions "

        
    def generate_daily_returns(self): 
        """For each position, simulate n daily returns, where n is num_trials """

        investment_outcome = []
        # Example with position = 10
        # Each day (simulation), need to generate 10 random investment outcomes
        # In total, generate position*num_trials investment outcomes. Get an array of length position*num_trials 
        for i in range(self.position*self.num_trials):
            
            #Each outcome is a Bernoulli with p = 0.51 (program as binomial with n=1)
            outcome_of_draw = np.random.binomial(1, 0.51)
            investment_outcome.append(self.position_value*2*outcome_of_draw)
        
        # Wrap the position*num_trials array so that have 'num_trials' rows and 'position' columns
        # To obtain daily cumulative return, sum over all columns. Obtain cumu_ret array of length 'num_trials'
        matrix_of_results = np.array(investment_outcome).reshape(self.position, self.num_trials).T
        cumu_ret = matrix_of_results.sum(axis=1)
        daily_ret =  (cumu_ret/1000)-1
        return daily_ret
    
    
    def histogram(self, daily_ret):
        """For each position, produce a histogram """
    
        # daily_ret array is "fixed" in assignment8.py
        plt.hist(daily_ret,100,range=[-1,1])
        plt.xlabel("Daily Return") 
        plt.ylabel("Distribution")
        plt.title("The histogram of the result for " + str(self.position) + self.position_word + "of $"+ str(int(self.position_value)))
        plt.xticks(fontsize=10) 
        plt.yticks(fontsize=10)
        label = "000" + str(self.position)
        plt.savefig('histogram_' + label[-4:] +'_pos.pdf')
        plt.clf()
        
    
    def summary_stats(self, daily_ret):
        """For each position, produce summary stats and save in results.txt created in assignment8.py """
    
        file = open("results.txt", "a") 
        mean = float(("{0:.5f}".format(daily_ret.mean())))
        std = float(("{0:.5f}".format(daily_ret.std())))
        
        file.write("RESULT FOR " + str(self.position) + self.position_word + "of $"+ str(int(self.position_value)) + '\n')
        file.write('Mean of the daily return:               ' + str(mean) + '\n')
        file.write('Standard deviation of the daily return: '+str(std) + '\n') 
        file.write('\n')
        file.close()
