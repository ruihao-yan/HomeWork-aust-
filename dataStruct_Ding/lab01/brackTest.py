import unittest
from brack import matchBrack
class unit(unittest.TestCase):
    def test_match(self):
        a = "({[<>]})"
        self.assertEqual(matchBrack(a), True, "match fully")
    
    def test_notMath(self):
        a = "({}]"
        self.assertEqual(matchBrack(a), False, "Not Math")

    def test_None(self):
        a = ""
        self.assertEqual(matchBrack(a), True, "fully Match")

    def test_odd(self):
        a = "{}{}["
        self.assertEqual(matchBrack(a), False, "odd")
 