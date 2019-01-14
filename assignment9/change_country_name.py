""" This module changes names of several countries in the 'countries' dataset to ensure they are matched with entries in the 'income' dataset. These changes are implemented only for the most obvious cases."""

import sys
import os
import pandas as pd
import numpy as np


def change_name(data):
    """ Change 14 country names in the 'countries' dataset to be consistent with 'income' dataset """

    updated_data =data.replace(to_replace = "Russian Federation", value = "Russia")                 #1 
    updated_data =updated_data.replace(to_replace = "Slovakia", value = "Slovak Republic")          #2
    updated_data =updated_data.replace(to_replace = "East Timor", value = "Timor-Leste")            #3
    updated_data =updated_data.replace(to_replace = "Burma", value = "Myanmar")                     #4
    updated_data =updated_data.replace(to_replace = "Micronesia", value = "Micronesia, Fed. Sts.")  #5
    updated_data =updated_data.replace(to_replace = "Macedonia", value = "Macedonia, FYR")          #6
    updated_data =updated_data.replace(to_replace = "Korea, South", value = "Korea, Rep.")          #7 
    updated_data =updated_data.replace(to_replace = "Korea, North", value = "Korea, Dem. Rep.")     #8
    updated_data =updated_data.replace(to_replace = "Dominican Republic", value = "Dominican Rep.") #9
    updated_data =updated_data.replace(to_replace = "Czech Republic", value = "Czech Rep.")         #10
    updated_data =updated_data.replace(to_replace = "Congo", value = "Congo, Rep.")                 #11 
    updated_data =updated_data.replace(to_replace = "Congo, Democratic Republic of", value = "Congo, Dem. Rep.") 
    updated_data =updated_data.replace(to_replace = "Central African Republic", value = "Central African Rep.")
    updated_data =updated_data.replace(to_replace = "Burkina", value = "Burkina Faso")              #14
    
    return updated_data
