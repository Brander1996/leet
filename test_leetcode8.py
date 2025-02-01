import unittest
from leetcode8 import Solution

class TestLeetcode8(unittest.TestCase): 
    def setUp(self):
        self.solution = Solution()

    def test_removeWhiteSpace(self):
        self.assertEqual(self.solution.removeWhiteSpace("    kaolo"), "kaolo")
        self.assertEqual(self.solution.removeWhiteSpace("f"), "f")
        self.assertEqual(self.solution.removeWhiteSpace(""), "")
        
    def test_removeSign(self):
        self.assertEqual(self.solution.removeSign("+"), "")
        self.assertEqual(self.solution.removeSign("-"), "")
        self.assertEqual(self.solution.removeSign("+hallo"), "hallo")
        self.assertEqual(self.solution.removeSign("-hallo"), "hallo")
        self.assertEqual(self.solution.removeSign("hallo"), "hallo")
        self.assertEqual(self.solution.removeSign(""), "")

    def test_skipZeros(self):
        self.assertEqual(self.solution.skipZeros("0000"),"")
        self.assertEqual(self.solution.skipZeros(""),"")
        self.assertEqual(self.solution.skipZeros("0010"),"10")
        self.assertEqual(self.solution.skipZeros("0ab0"),"ab0")
        
    def test_isNegative(self):
        self.assertEqual(self.solution.isNegative("-"), True)
        self.assertEqual(self.solution.isNegative("lkjl;"), False)
        self.assertEqual(self.solution.isNegative("+"), False)
        self.assertEqual(self.solution.isNegative(""), False)        
    
    def test_leadingDigits(self):
        self.assertEqual(self.solution.provideLeadingDigits("-342"),"")
        self.assertEqual(self.solution.provideLeadingDigits("lkjl;"),"")
        self.assertEqual(self.solution.provideLeadingDigits("234+jkh"),"234")
        self.assertEqual(self.solution.provideLeadingDigits(""),"")

    def test_rounNumber(self):
        self.assertEqual(self.solution.roundNumber(2147483647), 2147483647)
        self.assertEqual(self.solution.roundNumber(2147483646), 2147483646)
        self.assertEqual(self.solution.roundNumber(2147483648), 2147483647)
        self.assertEqual(self.solution.roundNumber(-2147483648), -2147483648)
        self.assertEqual(self.solution.roundNumber(-2147483649), -2147483648)        
        self.assertEqual(self.solution.roundNumber(-2147483646), -2147483646)
        self.assertEqual(self.solution.roundNumber(0), 0)  # Corrected
        self.assertEqual(self.solution.roundNumber(-1), -1)
        self.assertEqual(self.solution.roundNumber(1), 1)

    def test_myAtoi(self):
        self.assertEqual(self.solution.myAtoi("42"),42)
        self.assertEqual(self.solution.myAtoi("-042"),-42)
        self.assertEqual(self.solution.myAtoi("1337c0d3"),1337)
        self.assertEqual(self.solution.myAtoi("0-1"),0)
        self.assertEqual(self.solution.myAtoi("words and 987"),0)
        self.assertEqual(self.solution.myAtoi("-00002"),-2)
        self.assertEqual(self.solution.myAtoi("-   "),0)
        self.assertEqual(self.solution.myAtoi("    23   "),23)
        self.assertEqual(self.solution.myAtoi("    +23   "),23)
        self.assertEqual(self.solution.myAtoi("    -000002147483649asdfasgh"),-2147483648)                
        




        # is_negative =self.isNegative(without_whitespace)
        # without_sign = self.removeSign(without_whitespace)
        # without_zeros = self.skipZeros(without_sign)
        # digits= self.leadingDigits(without_zeros)
        # number = int(digits)