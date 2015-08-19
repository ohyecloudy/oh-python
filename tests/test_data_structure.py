# -*- coding: utf-8 -*-
import unittest

class TestList(unittest.TestCase):

    def test_indexed(self):
        arr = [1, 2, 3]
        self.assertEqual(3, arr[2])
        self.assertEqual(2, arr[-2])
        self.assertEqual(1, [1, 4, 5][0])

    def test_slicing(self):
        arr = [1, 2, 3, 4, 5]
        self.assertEqual([1, 2], arr[0:2])
        self.assertEqual([3, 4, 5], arr[-3:])
        self.assertEqual(arr, arr[:])

    def test_concatenate(self):
        arr = [1, 2]
        self.assertEqual([1, 2, 3, 4], arr + [3, 4])

    def test_mutable(self):
        arr = [1, 2, 3]
        arr[2] = 4
        self.assertEqual([1, 2, 4], arr)
        arr[1:3] = [3, 6]
        self.assertEqual([1, 3, 6], arr)
        arr[1:3] = []
        self.assertEqual([1], arr)

    def test_nested(self):
        arr = [1, 2]
        arr.append([3, 4])
        self.assertEqual([1, 2, [3, 4]], arr)
        self.assertEqual(4, arr[2][1])

    def test_append(self):
        arr = [1, 2]
        arr.append(3)
        self.assertEqual([1, 2, 3], arr)
        arr[len(arr):] = [4]
        self.assertEqual([1, 2, 3, 4], arr)

    def test_extend(self):
        arr = [1, 2]
        arr.extend([3, 4])
        self.assertEqual([1, 2, 3, 4], arr)
        arr[len(arr):] = [5, 6]
        self.assertEqual([1, 2, 3, 4, 5, 6], arr)

    def test_insert(self):
        arr = [1, 2]
        arr.insert(0, -1)
        self.assertEqual([-1, 1, 2], arr)
        arr.insert(1, 0)
        self.assertEqual([-1, 0, 1, 2], arr)
        arr.insert(len(arr), 3)
        self.assertEqual([-1, 0, 1, 2, 3], arr)

    def test_remove(self):
        arr = [1, 2]
        with self.assertRaises(ValueError):
            arr.remove(3) # 없는 element 삭제 시도시 ValueError
        arr.remove(2)
        self.assertEqual([1], arr)

    def test_pop(self):
        arr = [1, 2, 3, 4]
        self.assertEqual(4, arr.pop())
        self.assertEqual([1, 2, 3], arr)
        self.assertEqual(2, arr.pop(1))
        self.assertEqual([1, 3], arr)

    def test_index(self):
        arr = [1, 2, 3]
        with self.assertRaises(ValueError):
            arr.index(4) # 못 찾을 경우 ValueError
        self.assertEqual(1, arr.index(2))

    def test_count(self):
        arr = [1, 1, 1, 2]
        self.assertEqual(0, arr.count(3))
        self.assertEqual(3, arr.count(1))

    def test_sort(self):
        arr = [2, 1, 3, 4]
        arr.sort(lambda x,y: cmp(y, x))
        self.assertEqual([4, 3, 2, 1], arr, "cmp는 -1, 0, 1 함수를 사용해야 한다")
        arr.sort(lambda x,y: cmp(y, x), lambda x: -x)
        self.assertEqual([1, 2, 3, 4], arr, "key func로 비교 전 가공을 할 수 있다")
        arr.sort(lambda x,y: cmp(y, x), lambda x: -x, True)
        self.assertEqual([4, 3, 2, 1], arr, "reverse로 비교 결과를 뒤집을 수 있다")

    def test_reverse(self):
        arr = [2, 1, 3]
        arr.reverse()
        self.assertEqual([3, 1, 2], arr)

    def test_del(self):
        a = [1, 2, 3, 4]
        del a[0]
        self.assertEqual([2, 3, 4], a)
        del a[1:3]
        self.assertEqual([2], a)
        del a[:]
        self.assertEqual([], a)

class TestFunctionalProgrammingTools(unittest.TestCase):

    def test_filter(self):
        l = filter(lambda x: x % 2 == 0, range(5))
        self.assertEqual([0, 2, 4], l)

    def test_map(self):
        l = map(lambda x: x ** 2, range(5))
        self.assertEqual([0, 1, 4, 9, 16], l)
        l = map(lambda x,y: (x or 0) + (y or 0), range(5), range(4))
        self.assertEqual([0, 2, 4, 6, 4], l,
                         "map에서 길이가 다를 경우 None으로 들어온다")

    def test_reduce(self):
        s = reduce(lambda x,y: x + y, range(5))
        self.assertEqual(0 + 1 + 2 + 3 + 4, s)

class TestListComprehensions(unittest.TestCase):
    def test_for_create(self):
        self.assertEqual([0, 1, 4, 9], [x**2 for x in range(4)])
        self.assertEqual([(1, 2), (2, 1)],
                         [(x, y) for x in [1, 2] for y in [2, 1] if x != y])
        self.assertEqual([2, 1, 0, 1, 2], [abs(x) for x in [-2, -1, 0, 1, 2]])

    def test_for_nested(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8],
            [9, 10, 11, 12],
        ]
        self.assertEqual([[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]],
                         [[row[i] for row in matrix] for i in range(4)])

class TestTupleAndSequnces(unittest.TestCase):
    def test_tuples(self):
        t = "hello", 123, True
        self.assertEqual(123, t[1])
        x, y, z = t
        self.assertEqual(True, z, "tuple unpacking")

    def test_tuples_immutable(self):
        t = "hello", 123
        with self.assertRaises(TypeError):
            t[1] = 3 # immutable
        self.assertEqual(123, t[1])

class TestSet(unittest.TestCase):
    def test_set(self):
        r = [1, 2, 3, 2, 1, 3, 4, 2, 1]
        s = set(r)
        self.assertEqual(set([1, 2, 3, 4]), s)
        self.assertTrue(1 in s)
        self.assertTrue(8 not in s)

    def test_set_op(self):
        a = set('abcde')
        b = set('cdefg')
        self.assertEqual(set(['a', 'b']), a - b)
        self.assertEqual(set(['a', 'b', 'c', 'd', 'e', 'f', 'g']), a | b)
        self.assertEqual(set(['c', 'd', 'e']), a & b)
        self.assertEqual(set(['a', 'b', 'f', 'g']), a ^ b)

    def test_comprehensions(self):
        self.assertEqual(set(['d', 'e']),
                         {x for x in 'abcdedede' if x not in 'abc'})

class TestDictionary(unittest.TestCase):
    def test_dic(self):
        d = {'a':1, 'b':2}
        self.assertEqual(1, d['a'])
        d['c'] = 3
        self.assertEqual(3, len(d))
        del d['b']
        self.assertFalse('b' in d)

    def test_comprehensions(self):
        self.assertEqual({2: 4, 4: 16, 5: 25},
                         {x: x**2 for x in [2, 4, 5]})

class TestLoopingTechnique(unittest.TestCase):
    def test_enumerate(self):
        l = [(i, j) for i, j in enumerate(['a', 'b', 'c'])]
        self.assertEqual([(0, 'a'), (1, 'b'), (2, 'c')], l)

        l2 = [(i, j) for i, j in enumerate(['a', 'b', 'c'], 1)]
        self.assertEqual([(1, 'a'), (2, 'b'), (3, 'c')], l2,
                         "enumerate 두번째 인자로 시작 index를 넣을 수 있다.")

    def test_zip(self):
        a = ['a', 'b', 'c', 'd']
        b = [1, 2, 3]
        r = [(x, y) for x, y in zip(a, b)]
        self.assertEqual([('a', 1), ('b', 2), ('c', 3)], r,
                         "짧은 리스트 길이만큼 zip!")
        a2, b2 = zip(*r)
        self.assertEqual(('a', 'b', 'c'), a2)
        self.assertEqual((1, 2, 3), b2)

    def test_reversed(self):
        self.assertEqual([3, 2, 1, 0], list(reversed(xrange(4))))

    def test_sorted(self):
        a = [1, 3, 2]
        self.assertEqual([1, 2, 3], sorted(a), "a를 변경하지 않는다.")
        self.assertEqual([1, 3, 2], a)

    def test_iteritems(self):
        a = {'a': 1, 'b': 2}
        self.assertEqual(['a1', 'b2'], ["%s%s" %(x, y) for x, y in a.iteritems()])

if __name__ == '__main__':
    unittest.main()
