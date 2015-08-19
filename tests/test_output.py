# -*- coding: utf-8 -*-
import unittest
import math

class TestOutput(unittest.TestCase):
    def test_format(self):
        self.assertEqual('1, True, a', "{}, {}, {}".format(1, True, 'a'))
        self.assertEqual('b, a', "{1}, {0}".format('a', 'b'))
        self.assertEqual('a=b', "{key}={value}".format(key='a', value='b'))
        self.assertEqual('3.142', "{0:.3f}".format(math.pi))
        self.assertEqual('   1', "{:4}".format(1))

    def test_format_dict(self):
        self.assertEqual('a: 1, b: 2',
                         'a: {0[a]:d}, b: {0[b]:d}'.format({'a': 1, 'b': 2}),
                         '[]로 value에 바로 access할 수 있다')
        self.assertEqual('a: 1, b: 2',
                         'a: {a:d}, b: {b:d}'.format(**{'a': 1, 'b': 2}),
                         '**로 keyword arguments로 dict를 넘길 수 있다')

if __name__ == '__main__':
    unittest.main()
