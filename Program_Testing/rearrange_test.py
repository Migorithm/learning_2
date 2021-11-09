import unittest
#it has TestCase class with a bunch of testing methods. 


import rearrange


class TestRearrange(unittest.TestCase):
    #By inheriting TestCase, any methods defined in this TestRearrange class that start with the prefix 
    #'test' will become tests that can be run by the testing framework.
    def test_basic(self):
        testcase ="Lovelace, Ada"
        expected ="Ada Lovelace"
        self.assertEqual(rearrange.rearrange_name(testcase),expected)
    #assertEqual method basically says both of my arguments are equal. -> Bool.
    
    def test_empty(self):
        testcase=""
        expected=""
        self.assertEqual(rearrange.rearrange_name(testcase),expected)
    
unittest.main()