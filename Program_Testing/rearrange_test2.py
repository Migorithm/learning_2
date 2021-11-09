import unittest
import rearrange
#Check if string contains spaces or dot that will make our regular expression not match.


class TestRearrange(unittest.TestCase):
    def test_dot_space(self):
        testcase="Hopper, Grace M."
        expected="Grace M. Hopper"
        self.assertEqual(rearrange.rearrange_name(testcase),expected)
        
    #how about someone who has only one name?
    def test_one_name(self):
        testcase = "Voltaire"
        expected= "Voltaire"
        self.assertEqual(rearrange.rearrange_name(testcase),expected)
unittest.main()