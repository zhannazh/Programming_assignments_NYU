# assignment8.py (main): 

	# Processes inputs, handles errors, and calls the investment_instrument class
	# to produce daily returns, histograms, and statistics"

	# The program handles user-defined exceptions+KeyboardInterrupt+SystemExit
    
	### Takes 2 types of inputs: 
    	### 1. List of positions (comma-separated; no parentheses/brackets; 
	     only 1,10, 100, and 1000 are valid)
    	### 2. Number of simulations to be run (just an integer)         

# investment_instrument.py: 
    	# The class generates daily returns for each position and the specified number of simulations.
	# It also produces a histogram for each position (in a pdf file) and saves the mean and std of
	# daily returns for each position in results.txt file.
    	
	### investment_instrument.py takes (processed) inputs from assignment.py 
	### (a list of positions and the number of simulations)

# exceptions.py:
	# Specifies the types of exceptions that the program can handle

# tests.py
	# contains unittests

# References used in writing this program:
    
    #   Lecture notes
    #   Lutz book (Chapters on exception handling)
    #   https://www.programiz.com/python-programming/user-defined-exception
        # contains an example of how to handle exceptions

    #   http://www.pythonforbeginners.com/files/reading-and-writing-files-in-python
        # contains an example of how to write files in a loop
    
    #   https://docs.scipy.org/doc/numpy/reference/generated/numpy.random.binomial.html
        # explains that random.binomial should be used when we want to generate a Bernoulli with p !=0.50
        
    #   http://matplotlib.org/1.3.1/users/index.html
    #   https://docs.python.org/2/library/random.html
    #   https://docs.python.org/2/library/functions.html#float
    #   https://docs.python.org/3/tutorial/errors.html
    #   https://docs.python.org/3/library/exceptions.html
    #   https://docs.python.org/2/library/re.html
    #   https://docs.python.org/3.4/library/unittest.html
 