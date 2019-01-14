
# coding: utf-8

# In[1]:

import unittest
import interval as interval
import numpy as np


class Test1(unittest.TestCase):
    
    def test_interval(self):
        self.assertEqual(interval.interval('[0,0]').values,0)
        self.assertEqual(interval.interval('(1,2]').min_, 2)
        self.assertEqual(interval.interval('(1,2]').max_, 2)
        self.assertEqual(interval.interval('(1,2]').lower_bracket, '(')
        self.assertEqual(str(interval.interval('(1,5)').values), str(np.array([2, 3, 4])))
        self.assertEqual(interval.interval('[2,3]').min_,2)
        
        self.assertRaises(ValueError, interval.interval, '(10,8)')
        self.assertRaises(ValueError, interval.interval, '(0,0)')

class Test2(unittest.TestCase):
    
    def test_mergeIntervals(self):
        self.assertEqual(str(interval.mergeIntervals("[1,5]", "[2,6)")), '[1, 6)')
        self.assertEqual(str(interval.mergeIntervals("(8,10]", "[8,18]")), '[8, 18]')
        self.assertEqual(str(interval.mergeIntervals("(0,3]", "[2,5)")), '(0, 5)')
        
        self.assertRaises(ValueError, interval.mergeIntervals, interval.interval('[1,2]'), interval.interval('[3,4)'))
        self.assertRaises(ValueError, interval.mergeIntervals, interval.interval('[1,2]'), interval.interval('(0,1)'))
        
        
class Test3(unittest.TestCase):
    
    def test_mergeOverlapping(self):
        self.assertEqual(str(interval.mergeOverlapping(['[-10, -7]', '(-4, 1]', '[3, 6)', '(8,12)', "[15,23]", "[4,8]"])), '[[-10, -7], (-4, 1], [3, 12), [15, 23]]')
        self.assertEqual(str(interval.mergeOverlapping(["[1,5]", "[2,6)", "(8,10]", "[8,18]"])), '[[1, 6), [8, 18]]')
        
        self.assertRaises(ValueError, interval.mergeOverlapping, ["[1,5]", "[2,6)", "(8,10]", "(0,0)"])
        
class Test4(unittest.TestCase):
    
    def test_insert(self):
        self.assertEqual(str(interval.insert(["[1,3]", "[6,9]", "[3,6)"], "[2,5]")), '[[1, 9]]')
        self.assertEqual(str(interval.insert(["[-10,-7]", "(-4,1]", "[3,6)","(5,12)","[11,23]"],"[4,8]")), '[[-10, -7], (-4, 1], [3, 23]]')
        
        self.assertRaises(ValueError, interval.insert, ["[1,3]", "[6,9]", "[3,6)"], interval.interval('(0,1)'))
        
        
        
        
if __name__ == '__main__':
    unittest.main()
 
