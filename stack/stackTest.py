import unittest
from sequenceStack import  sequenceStack

class Test(unittest.TestCase):
    def test_insert(self):
        stack = sequenceStack()
        stack.add("one")
        stack.add("second")
        stack.add("third")
        self.assertEqual("third -> second -> one", stack.__str__())

    def test_get(self):
        stack = sequenceStack()
        stack.add("one")
        stack.add("second")
        stack.add("third")
        self.assertEqual(stack.__str__(), "third -> second -> one")
        self.assertEqual(stack.delete(), "third")
        self.assertEqual(stack.__str__(), "second -> one")
        self.assertEqual(stack.delete(), "second")
        self.assertEqual(stack.delete(), "one")
        with self.assertRaises(AssertionError):
            self.assertEqual(stack.delete())

    def test_reSize(self):
        stack = sequenceStack()
        stack.add("one")
        stack.add("second")
        stack.add("third")
        stack.add("one")
        stack.add("second")
        stack.add("third")
        stack.add("one")
        stack.add("second")
        stack.add("third")
        stack.add("one")
        stack.add("second")
        stack.add("third")
        self.assertEqual("third -> second -> one -> third -> second -> one -> third -> second -> one -> third -> second -> one", stack.__str__())

        