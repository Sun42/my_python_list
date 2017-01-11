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

if __name__ == "__main__":
    unittest.main()
