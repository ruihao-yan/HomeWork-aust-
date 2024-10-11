from LinkList import LinkList
import unittest
class Test(unittest.TestCase):
    def test_Length(self):
        a = LinkList('eight', None)
        a.addList('seven')
        a.addList('six')
        a.addList('five')
        a.addList('four')
        a.addList('three')
        a.addList('two')
        a.addList('one')
        self.assertEqual(a.length(), 8, 'testLength')

    def test_isNone(self):
        a = LinkList('eight', None)
        a.addList('seven')
        a.addList('six')
        a.addList('five')
        a.addList('four')
        a.addList('three')
        a.addList('two')
        a.addList('one')
        self.assertFalse(a.isNone(), 'testIsNone')
    
    def test_print(self):
        a = LinkList('eight', None)
        a.addList('seven')
        a.addList('six')
        a.addList('five')
        a.addList('four')
        a.addList('three')
        a.addList('two')
        a.addList('one')
        self.assertEqual(a.__str__(), 'one -> two -> three -> four -> five -> six -> seven -> eight -> None')
    
    def test_search(self):
        a = LinkList('eight', None)
        a.addList('seven')
        a.addList('six')
        a.addList('five')
        a.addList('four')
        a.addList('three')
        a.addList('two')
        a.addList('one')
        self.assertEqual(a.search('four'), 3, 'search location')
    
    def test_del(self):
        a = LinkList('eight', None)
        a.addList('seven')
        a.addList('six')
        a.addList('five')
        a.addList('four')
        a.addList('three')
        a.addList('two')
        a.addList('one')
        self.assertEqual(a.__str__(), 'one -> two -> three -> four -> five -> six -> seven -> eight -> None')
        a.delList(3)
        self.assertEqual(a.__str__(), 'one -> two -> three -> five -> six -> seven -> eight -> None')
        a.delList(0)
        self.assertEqual(a.__str__(), 'two -> three -> five -> six -> seven -> eight -> None')
        a.delList(0)
        a.delList(0)
        a.delList(0)
        a.delList(0)
        self.assertEqual(a.__str__(), 'seven -> eight -> None')
        a.delList(0)
        self.assertEqual(a.__str__(), 'eight -> None')
        a.delList(0)
        self.assertEqual(a.__str__(), 'None')

    def test_delNode(self):
        a = LinkList('one', None)
        a.delList(0)
        with self.assertRaises(AssertionError):
            a.delList(0) 
    
    def test_add(self):
        a = LinkList('eight', None)
        a.addList('seven')
        a.addList('six')
        a.addList('five')
        a.addList('four')
        a.addList('three')
        a.addList('two')
        a.addList('one')
        a.addListInend('nine')
        self.assertEqual(a.__str__(), 'one -> two -> three -> four -> five -> six -> seven -> eight -> nine -> None')
        self.assertEqual(a.length(), 9, 'test Length')

unittest.main()
    

    
