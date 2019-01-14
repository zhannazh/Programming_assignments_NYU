Author: zvz201
Date: December 3, 2016

# assignment9.py (main): 

	This module contains the main program that produces output as specified in assignment 9

	# The program handles user-defined exceptions+KeyboardInterrupt+SystemExit (when ask for input)
	# Correct year input is either an integer between 1800 and 2012 or "finish"
	# To exit the program, the user can type "quit" or "exit" 

# change_country_name.py: 
	This module changes names of 14 countries in the 'countries' dataset to ensure they are
	matched with entries in the 'income' dataset. These changes are implemented only for 
	the most obvious cases (e.g., changed "Russian Federation" to "Russia").

# data_analysis.py:
	This class module generates two types of by-region histograms and one type of boxplots
	for the given year

# exceptions.py:
	The module specifies the types of exceptions that the program can handle:
	 - Elements other than digits (or negative)
	 - Input is out of range
   	 - No input
	 - Various types of program exits

# process_input.py:
	The module handles the user's input of Year and raises exceptions when encountered

# results.txt contains a short description for Question 9

# tests.py
	# contains unittests

# References used in writing this program:
    
- Lecture notes
- Lutz book (part V)
- http://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_excel.html
- http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.sort_values.html
- http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
- http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.replace.html
- http://matplotlib.org/api/pyplot_api.html
- https://docs.scipy.org/doc/numpy/reference/generated/numpy.histogram.html
- http://pandas.pydata.org/pandas-docs/stable/reshaping.html
- http://seaborn.pydata.org/generated/seaborn.FacetGrid.html
- http://seaborn.pydata.org/generated/seaborn.axes_style.html#seaborn.axes_style
- http://pandas.pydata.org/pandas-docs/version/0.18.1/visualization.html
- http://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.html
- http://matplotlib.org/examples/statistics/histogram_demo_multihist.html
- https://docs.python.org/3.4/library/unittest.html
 