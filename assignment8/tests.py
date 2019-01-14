"""This module tests correctness of outputs in the investment_instrument.py module. """
""" assignment8.py runs in a user-interactive mode, and basic entry errors are raised as exceptions until the user enters the correct input """

import unittest
import investment_instrument as invest
import numpy as np
import exceptions
import re

class Test(unittest.TestCase):
    
    def test_number_of_simulations(self):
        """ test whether obtain the correct number of daily returns"""
        self.assertEqual(len(invest.investment_instrument(100,120).generate_daily_returns()), 120)

    def test_type_of_returns(self):
        """ test whether obtain the correct types of returns"""
        self.assertTrue(np.array_equal(np.unique(invest.investment_instrument(1,1000).generate_daily_returns()), np.array([-1,1])))
                         
    def test_type_of_returns_more_detailed(self):
        """ test whether obtain the correct types of returns - more entries"""
        returns = invest.investment_instrument(10,1000).generate_daily_returns()
        self.assertGreater(len(re.findall('-0.2', str(returns))),0)
                             
    def test_maximum(self):
        """ test whether obtain correct max"""
        self.assertLessEqual(np.max(invest.investment_instrument(100,200).generate_daily_returns()), 1)

    def test_minimum(self):
        """ test whether obtain correct min"""
        self.assertGreaterEqual(np.min(invest.investment_instrument(100,200).generate_daily_returns()), -1)
        
if __name__ == '__main__':
    unittest.main()
 
