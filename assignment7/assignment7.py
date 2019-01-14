

#import useful packages
import sys
import numpy as np
import re
from interval import *

if __name__ == '__main__':
   
    print("List of intervals?")
    print("Please follow this format: [1,2], [2,3]")
    input_interval_list = str(input())
    interval_list_no_white_space = input_interval_list.replace(" ", "")
    
    def input_has_letters(string):
        if re.search('[a-zA-Z]', string):
            return True
    
    def input_has_nonintegers(string):
        if re.search('[.]', string):
            return True   
        
    def lower_bound_greater_than_upper(element):
        if element.min_ > element.max_:
            return True    
        
    def empty_set(element):
        if element.values is "":
            return True    

    def input_has_curly_bracket_lower(string):
        if re.search('{', string):
            return True
        
    def input_has_curly_bracket_upper(string):
        if re.search('}', string):
            return True

    while input_has_letters(interval_list_no_white_space) and interval_list_no_white_space!="quit":
        print('Invalid interval(s)')
        print("List of intervals?")
        input_interval_list = str(input())
        interval_list_no_white_space = input_interval_list.replace(" ", "")
        continue

    while input_has_nonintegers(interval_list_no_white_space) and interval_list_no_white_space!="quit":
        print('Invalid interval(s)')
        print("List of intervals?")
        input_interval_list = str(input())
        interval_list_no_white_space = input_interval_list.replace(" ", "")
        continue
        
        
    while input_has_curly_bracket_lower(interval_list_no_white_space) and interval_list_no_white_space!="quit":
        print('Invalid interval(s)')
        print("List of intervals?")
        input_interval_list = str(input())
        interval_list_no_white_space = input_interval_list.replace(" ", "")
        continue
        
    while input_has_curly_bracket_upper(interval_list_no_white_space) and interval_list_no_white_space!="quit":
        print('Invalid interval(s)')
        print("List of intervals?")
        input_interval_list = str(input())
        interval_list_no_white_space = input_interval_list.replace(" ", "")
        continue

    if interval_list_no_white_space == "quit":
        sys.exit(0)
    
              
    intervals_list = []
    for i in ["\[","\("]:
        for j in ["\]","\)"]:
            #pattern = re.compile(i+'.[0-9]+,.[0-9]+' +j)
            pattern1 = re.compile(i+'[0-9]+,[0-9]+' +j)
            pattern2 = re.compile(i+'-[0-9]+,[0-9]+' +j)
            pattern3 = re.compile(i+'-[0-9]+,-[0-9]+' +j)
            pattern4 = re.compile(i+'[0-9]+,-[0-9]+' +j)

            find_intervals1 = re.findall(pattern1, interval_list_no_white_space)
            find_intervals2 = re.findall(pattern2, interval_list_no_white_space)
            find_intervals3 = re.findall(pattern3, interval_list_no_white_space)
            find_intervals4 = re.findall(pattern4, interval_list_no_white_space)

            intervals_list.extend(find_intervals1)
            intervals_list.extend(find_intervals2)
            intervals_list.extend(find_intervals3)
            intervals_list.extend(find_intervals4)
    
    
    for i in intervals_list:
        if lower_bound_greater_than_upper(interval(str(i))) or empty_set(interval(str(i))):
            raise ValueError('Invalid interval')
            # Not sure how to override the error prompted from the interval class so 
            # that the program can ask for new input

    try:
        
        print("Interval?")
        user_choice_one_interval = str(input())
        one_interval_no_space = user_choice_one_interval.replace(" ", "")
    
        while input_has_letters(one_interval_no_space) and one_interval_no_space!="quit":
            print('Invalid interval')
            print("Interval?")
            user_choice_one_interval = str(input())
            one_interval_no_space = user_choice_one_interval.replace(" ", "")
            continue
            
        while one_interval_no_space  != "quit":    
            while not input_has_letters(one_interval_no_space): 
                result = insert(intervals_list, user_choice_one_interval)
                print(result)
                print("Interval?")
                user_choice_one_interval = str(input())
                one_interval_no_space = user_choice_one_interval.replace(" ", "")

            else: 
                if one_interval_no_space != "quit":
                    print("Invalid interval")
                    print("Interval?")
                    user_choice_one_interval = str(input())
                    one_interval_no_space = user_choice_one_interval.replace(" ", "")
                else:
                    break
   
    except ValueError:
        print("Invalid interval. Start again.")