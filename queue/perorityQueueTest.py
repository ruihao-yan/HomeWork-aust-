from perorityQueue import MinHeap
import unittest
class Test(unittest.TestCase):
    def test_add(self):
        a = MinHeap()
        a.add(1)
        a.add(2)
        a.add(3)
        a.add(4)
        self.assertEqual([None, 1, 2, 3, 4], a._display())
        a.add(0)
        self.assertEqual([None, 0, 1, 3, 4, 2], a._display())
        a.add(-1)
        a.add(-2)
        self.assertEqual([None, -2, 1, -1, 4, 2, 3, 0], a._display())
        a.add(-3)
        self.assertEqual([None, -3, -2, -1, 1, 2, 3, 0, 4], a._display())

    def test_layer(self):
        a = MinHeap()
        self.assertEqual(2, a._layer(5))
        self.assertEqual(4, a._layer(23))
        self.assertEqual(0, a._layer(0))
        self.assertEqual(0,a._layer(1))
        self.assertEqual(3,a._layer(8))
        self.assertEqual(3, a._layer(15))
        self.assertEqual(4, a._layer(20))
        self.assertEqual(4, a._layer(16))

    def test_remove(self):
        a = MinHeap()
        a.add(1)
        a.add(2)
        a.add(3)
        a.add(4)
        self.assertEqual(1, a.offer())
        self.assertEqual([None, 2, 3, None], a._display())