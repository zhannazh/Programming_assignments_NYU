


#import useful packages
import sys
import numpy as np
import re


class interval:
    
    def __init__(self, interval_string):

        # Check whether the inputted interval is valid and process the interval string for output
        
        # Check that the input is a string (this will prompt an error is a digit is entered)
        if type(interval_string) != str:
            raise ValueError('Input must be a valid interval string, i.e. "[1,4]"')
        else:
            self.interval_input = interval_string
            # Delete white space
            self.interval_no_white_space = self.interval_input.replace(" ", "")

        # Check and code the type of the lower and upper parantheses / brackets 
        if self.interval_no_white_space[0] == "[" or self.interval_no_white_space[0] == "(":
            self.lower_bracket = self.interval_no_white_space[0]
        else:
            raise ValueError('First non-empty element in input cannot be must be either [ or ( ' % self.interval_no_white_space[0])

        if self.interval_no_white_space[-1] == "]" or self.interval_no_white_space[-1] == ")":
            self.upper_bracket = self.interval_no_white_space[-1]
        else:
            raise ValueError('Last non-empty element in input cannot be %s but must be either ] or ) ' % self.interval_no_white_space[-1])

        # Check that numbers are separated by a comma    
        if ',' in self.interval_no_white_space:        
            self.interval_split = self.interval_no_white_space[1:-1].split(',')
        else: 
            raise ValueError('Elements of the interval %s must be separated by comma and there must be 2 elements' % self.interval_input)

        # Check that the interval contains only 2 numbers (and define them)
        if len(self.interval_split) ==2:
                self.low_value_candidate=self.interval_split[0]
                self.hi_value_candidate=self.interval_split[1]
        else:
            raise ValueError('Interval %s can contain only two numbers and a comma' % self.interval_input)
        
        # Check that the numbers are integers. 
        # For each interval, define lower/upper bounds (these are the numbers that "show up" and can
        # be different from the interval's true min/max values)

        if float(self.low_value_candidate).is_integer() and float(self.hi_value_candidate).is_integer():
            self.low_value = int(self.low_value_candidate)
            self.hi_value = int(self.hi_value_candidate)
        else:
            raise ValueError('Interval %s must contain only integers' % self.interval_input)

        # Check that the lower bound is not greater than the upper bound
        if self.low_value > self.hi_value:
            raise ValueError('Lower bound (%s) cannot exceed the upper bound (%s)' % (self.low_value_candidate, self.hi_value_candidate))
               
                                
        # Below, construct intervals (to be outputted) based on their values and brackets/parantheses
        # For each interval, define "values" (numbers contained in the interval), "min," and "max"

        # CASES WHERE LOWER BOUND == UPPER BOUND
        # A case like (1,1) will be read as empty interval
        # A case like (1,1] or [1,1) will be read as an incorrect interval
        # A case like [1,1] will be read as [1]
        if self.low_value == self.hi_value:
            if self.lower_bracket == '[' and self.upper_bracket == ']':
                self.values, self.min_, self.max_ = self.low_value,self.low_value,self.low_value     
            else:
                raise ValueError('Interval %s is not valid' % self.interval_input)

        # CASES WHERE LOWER BOUND == UPPER BOUND-1
        # A case like (0,1] will be read as [1]
        # A case like [0,1) will be read as [0]
        # A case like (0,1) will be read as empty interval       
        elif self.low_value == self.hi_value-1:
            if self.lower_bracket == '(' and self.upper_bracket == ']':
                self.values, self.min_, self.max_ = self.hi_value,self.hi_value,self.hi_value
            
            elif self.lower_bracket == '[' and self.upper_bracket == ')':
                self.values, self.min_, self.max_ = self.low_value,self.low_value,self.low_value
            
            elif self.lower_bracket == '(' and self.upper_bracket == ')':
                self.values,self.min_, self.max_ = "","",""
            else:
                self.values = [self.low_value,self.hi_value]
                self.min_, self.max_ = self.values[0], self.values[-1]

        # REST OF THE CASES WHERE LOWER BOUND < UPPER BOUND-1
        elif self.low_value < self.hi_value-1:
        
            if self.lower_bracket == '(' and self.upper_bracket == ']':
                self.values = np.array(range(self.low_value+1, self.hi_value+1))

            elif self.lower_bracket == '[' and self.upper_bracket == ')':
                self.values = np.array(range(self.low_value, self.hi_value))
            
            elif self.lower_bracket == '(' and self.upper_bracket == ')':
                self.values = np.array(range(self.low_value+1, self.hi_value))
            
            else:
                self.values = np.array(range(self.low_value, self.hi_value+1))

            self.min_,self.max_ = self.values[0], self.values[-1]    
    
    # Aside: Construct a "unique ID" for each interval to be used later in sorting (and dictionary) 
        if self.values is not "":
            self.ID_temp =int(str(abs(self.min_)) + str(abs(self.low_value)) + str(abs(self.hi_value)) + str(abs(self.max_))) 
        else:
            self.ID_temp =int(str(abs(self.low_value)) + str(abs(self.low_value)) + str(abs(self.hi_value)) + str(abs(self.hi_value))) 
                
        if self.low_value >0:
            self.ID = self.ID_temp 
        elif self.low_value < 0 and self.hi_value >0:
            self.ID = -self.ID_temp
        else:
            self.ID = -int(str(self.ID_temp)+"999")
        
    # Construct output of class interval     
    def __repr__(self):
        return  '%s%s, %s%s' % (self.lower_bracket, self.low_value, self.hi_value, self.upper_bracket)



###

def mergeIntervals(int1,int2):
    
    # Check that inputs are strings
    if type(int1) != str or type(int2) != str:
            raise ValueError('Inputs must be valid interval strings, i.e. "[1,4]" ')
    else:
        int1 = interval(int1)
        int2 = interval(int2)
        
    # Regular case involves non-empty intervals (empty intervals are handled separately below)            
    def regular_case(int1,int2):

        # Check that the inputs are overlapping intervals. If not, ask to re-enter intervals
        if int1.max_ < int2.min_ or int2.max_ < int1.min_: 
            raise ValueError('Intervals %s and %s are non-overlapping. Please try again.' % (int1, int2))      
        
        # Construct the lower bound and lower bracket/parenthesis of the new merged interval
        if int1.min_ < int2.min_:
            new_lower_bracket = int1.lower_bracket
            new_low_value = int1.low_value
            
        elif int1.min_ > int2.min_:
            new_lower_bracket = int2.lower_bracket
            new_low_value = int2.low_value
        
        elif int1.min_ == int2.min_ and int1.low_value > int2.low_value:
            new_lower_bracket = int1.lower_bracket
            new_low_value = int1.low_value
            
        else:
            new_lower_bracket = int2.lower_bracket
            new_low_value = int2.low_value


        # Construct the upper bound and upper bracket/parenthesis of the new merged interval
        if int1.max_ > int2.max_:
            new_upper_bracket = int1.upper_bracket
            new_hi_value = int1.hi_value
        
        elif int1.max_ < int2.max_:
            new_upper_bracket = int2.upper_bracket
            new_hi_value = int2.hi_value

        elif int1.max_ == int2.max_ and int1.hi_value < int2.hi_value:
            new_upper_bracket = int2.upper_bracket
            new_hi_value = int2.hi_value

        else:
            new_upper_bracket = int1.upper_bracket
            new_hi_value = int1.hi_value
            
        # Construct new merged interval in the regular case   
        construct_interval_intermediate_step = '%s%s, %s%s' % (new_lower_bracket, new_low_value, new_hi_value, new_upper_bracket)
        resulting_interval = interval(construct_interval_intermediate_step)
        
        return resulting_interval
    
        
    #Check for any special cases (empty intervals) and handle appropriately:
    #"(0,0)" and "(0,1)" will give an empty set
    #"[0,0]" and "(0,1)" will give [0,0]
    
    if int1.values is "" and int2.values is "":
        merged_interval = ""
    
    elif int1.values is "" and int2.values is not "":
        merged_interval = int2
            
    elif int1.values is not "" and int2.values is "":
        merged_interval = int1
     
    else:
        merged_interval = regular_case(int1,int2)
    
    #Final return
    return merged_interval  
    


###

def mergeOverlapping(intervals):
   
    #Check if inputs are valid
    for i in intervals:
        if type(i) != str:
            raise ValueError('Inputs must be valid interval strings, i.e. "[1,4]" ')
 
    sequence = np.array(intervals)
    
    #Form a dictionary in order to sort the elements by the lower bound
    d= {}
    for i in sequence:
        interval_input = interval(str(i))
        d.update({interval_input.ID:interval_input}) #ID was defined in the interval class
    
    # Ordered sequence is the original sequence of intervals ordered by the lower bound
    ordered_sequence = []
    for key in sorted(d.keys()):
        ordered_sequence.append(d[key])
    
    # Start a new_interval where the first element is the first interval in the ordered sequence
    new_interval = interval(str(ordered_sequence[0]))
    
    # Store final output here
    resulting_sequence_of_intervals = []
    
    # Iterate through the remaining intervals in the ordered sequence
    for i in range(1,len(ordered_sequence[1:])+1):
        
        interval_input = interval(str(ordered_sequence[i]))
        
        
        # If the preceeding interval does not overlap with the current interval
        # store the preceeding in the resulting_sequence_of_intervals
        # and store current as new (for the next interation)
        if new_interval.max_ < interval_input.min_-1:
            resulting_sequence_of_intervals.append(new_interval)
            new_interval = interval_input
            #if the last  interval does not overlap with the preceeding result, save it
            if i==len(ordered_sequence[1:]):
                resulting_sequence_of_intervals.append(interval_input)

        elif new_interval.max_ == interval_input.min_-1:
            new_interval_intermed = new_interval.lower_bracket+str(new_interval.low_value) + ","+ str(interval_input.hi_value) + interval_input.upper_bracket
            new_interval = interval(str(new_interval_intermed))
            # if we reached the end of the sequence, save the last updated result
            if i==len(ordered_sequence[1:]):
                resulting_sequence_of_intervals.append(new_interval)                  

        # If the preceeding interval overlaps with the current interval
        # merge the intervals and store them as new for the next iteration
        else:
            new_interval = mergeIntervals(str(new_interval),str(interval_input))
            # if we reached the end of the sequence, save the last updated result
            if i==len(ordered_sequence[1:]):
                resulting_sequence_of_intervals.append(new_interval)    
        
    return resulting_sequence_of_intervals

###

def insert(intlist, newint):  
    
    #Check if inputs are valid
    for i in intlist:
        if type(i) != str:
            raise ValueError('Inputs must be valid interval strings, i.e. "[1,4]" ')

    if type(newint) != str:
        raise ValueError('Inputs must be valid interval strings, i.e. "[1,4]" ')

    
    intlist.append(str(newint))
    
    intervals_list = mergeOverlapping(intlist)
    
    return intervals_list



# References used:
# - Lecture notes
# - Lutz book
# - https://docs.python.org/2/library/re.html
# - https://docs.python.org/3.3/tutorial/errors.html
# 

