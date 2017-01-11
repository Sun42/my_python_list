#!/usr/bin/python3

import unittest
from mylist import MyList

class TestMyList(unittest.TestCase):

    def test_init(self):
        # given // when
        list_1 = MyList()
        list_2 = MyList([1, 2, 3])
        list_3 = MyList()
        list_3.append('a')
        list_3.append('b')

        # then
        self.assertEqual(list_1.length, 0)
        self.assertEqual(list_2.length, 3)
        self.assertEqual(list_3.length, 2)

    def test_str(self):
        # given
        list_1 = MyList()
        list_2 = []

         # then
        self.assertEqual(str(list_1), str(list_2))

        # when
        list_1.append('abc')
        list_2.append('abc')

        # then
        self.assertEqual(str(list_1), str(list_2))

        # when
        list_1.append(['d', 'e', 'f'])
        list_2.append(['d', 'e', 'f'])

        # then
        self.assertEqual(str(list_1), str(list_2))

    def test_index(self):
        # given
        list_1 = [1, 2, 3, 4, 5]
        list_2 = MyList(list_1)
        # when

        # then
        self.assertEqual(list_1.index(1), list_2.index(1))
        self.assertEqual(list_1.index(2), list_2.index(2))
        self.assertEqual(list_1.index(3), list_2.index(3))
        self.assertEqual(list_1.index(4), list_2.index(4))
        self.assertEqual(list_1.index(5), list_2.index(5))
        self.assertRaises(ValueError, list_1.index, 0)
        self.assertRaises(ValueError, list_2.index, 0)

    def test_count(self):
        # given
        list_1 = [1, 2, 2, 3, 3, 3]
        list_2 = MyList(list_1)

        # then
        self.assertEqual(list_1.count(0), list_2.count(0))
        self.assertEqual(list_1.count(1), list_2.count(1))
        self.assertEqual(list_1.count(2), list_2.count(2))
        self.assertEqual(list_1.count(3), list_2.count(3))

    def test_is_in(self):
        # given
        list_1 = MyList(['a', 1, ['nested', 'list']])

        # then
        self.assertEqual(True, list_1.is_in('a'))
        self.assertEqual(False, list_1.is_in('b'))
        self.assertEqual(True, list_1.is_in(1))
        self.assertEqual(False, list_1.is_in(2))
        self.assertEqual(True, list_1.is_in(['nested', 'list']))

    def test_extend(self):
        # given
        list_1 = MyList(['a', 'b', 'c'])
        # when
        list_1.extend(['d', 'e', 'f'])
        # then
        self.assertEqual(list_1.length, 6)
        self.assertEqual(list_1.index('a'), 0)
        self.assertEqual(list_1.index('b'), 1)
        self.assertEqual(list_1.index('c'), 2)
        self.assertEqual(list_1.index('d'), 3)
        self.assertEqual(list_1.index('e'), 4)
        self.assertEqual(list_1.index('f'), 5)

    def test_insert(self):
        # given
        list1  = MyList()
        # when
        list1.insert(0, 'a')
        # then
        self.assertEqual(list1.length, 1)
        self.assertEqual(list1.index('a'), 0)

        # when
        list1.insert(1, 'c')
        # then
        self.assertEqual(list1.length, 2)
        self.assertEqual(list1.index('a'), 0)
        self.assertEqual(list1.index('c'), 1)

        # when
        list1.insert(999, 'd')
        # then
        self.assertEqual(list1.length, 3)
        self.assertEqual(list1.index('a'), 0)
        self.assertEqual(list1.index('c'), 1)
        self.assertEqual(list1.index('d'), 2)

        # when
        list1.insert(0, '!')
        # then
        self.assertEqual(list1.length, 4)
        self.assertEqual(list1.index('!'), 0)
        self.assertEqual(list1.index('a'), 1)
        self.assertEqual(list1.index('c'), 2)
        self.assertEqual(list1.index('d'), 3)

if __name__ == "__main__":
    unittest.main()
