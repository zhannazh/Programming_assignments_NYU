"""This module tests correctness of inputs, including exceptions, and whether country renaming was carried out properly. """


import unittest
import pandas as pd
import numpy as np
import data_analysis
import exceptions
import process_input as inp
import change_country_name as change

class Test(unittest.TestCase):

        def test_correct_input(self):
            """ Check whether correct input is processed correctly"""
            self.assertEqual(inp.process_input('finish'), 'finish')
            self.assertEqual(inp.process_input('1998'), 1998)
            self.assertEqual(inp.process_input('1800'), 1800)

        def test_incorrect_input(self):
            """ Check whether incorrect input is processed correctly"""
            self.assertFalse(inp.process_input(')'))
            self.assertFalse(inp.process_input('-200'))
            self.assertFalse(inp.process_input('food'))
            self.assertFalse(inp.process_input('0'))
            self.assertFalse(inp.process_input('2014'))

        def test_exception(self):
            """ Check whether exception is raised"""
            self.assertRaises(SystemExit, inp.process_input, 'EXIT')
            self.assertRaises(SystemExit, inp.process_input, 'quit')

        def test_country_name_1(self):
            """ Check whether country name was correctly renamed pre-merge"""
            data = pd.DataFrame(['Russian Federation', 'Macedonia', 'Burkina'], columns=['Country'])
            self.assertEqual(list(data.Country[data.Country=='Russian Federation'].values),['Russian Federation'])
            self.assertEqual(list(change.change_name(data).Country[data.Country=='Russian Federation'].values),['Russia'])
                                
        def test_country_name_2(self):
            """ Check whether country name was correctly renamed pre-merge"""
            data = pd.DataFrame(['Russian Federation', 'Macedonia', 'Burkina'], columns=['Country'])
            self.assertEqual(list(data.Country[data.Country=='Macedonia'].values),['Macedonia'])
            self.assertEqual(list(change.change_name(data).Country[data.Country=='Macedonia'].values),['Macedonia, FYR'])

        def test_country_name_3(self):
            """ Check whether country name was correctly renamed pre-merge"""
            data = pd.DataFrame(['Russian Federation', 'Macedonia', 'Burkina'], columns=['Country'])
            self.assertEqual(list(data.Country[data.Country=='Burkina'].values),['Burkina'])
            self.assertEqual(list(change.change_name(data).Country[data.Country=='Burkina'].values),['Burkina Faso'])

if __name__ == '__main__':
    unittest.main()
 