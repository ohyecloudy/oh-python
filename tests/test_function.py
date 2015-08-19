# -*- coding: utf-8 -*-
import unittest

def null_func():
    pass

def f(a, L=[]):
    L.append(a)
    return L

# default value가 공유되는 걸 막으려면 안에서 새로 할당
def ff(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L

def sum_func(*arguments):
    ret = 0
    for i in arguments:
        ret += i
    return ret

def sum_values(**d):
    # doc string 예제. git commit 메시지 쓰듯이 쓰면 된다
    """dict의 values를 더한 값을 리턴

    key는 뭐가 들어오던지 말던지 신경 안 쓴다.
    """
    return sum_func(*d.values()) # list를 arguments로 unpacking

class TestFunction(unittest.TestCase):
    def test_return_none(self):
        self.assertEqual(None, null_func(), "리턴 값이 없는 procedure인 경우 None")

    def test_default_arg(self):
        self.assertEqual([1], f(1))
        self.assertEqual([1, 2], f(2),
                         "default value는 최초 한번 evaluation 된다."
                         "최초 evaluation된 []이 계속 사용됨")
        self.assertEqual([2], f(2, []))

    def test_default_arg_best_practice(self):
        self.assertEqual([1], ff(1))
        self.assertEqual([2], ff(2))

    def test_keyword_arguments(self):
        # named, optional arguments라고도 부른다
        self.assertEqual([10], ff(a=10))
        arr = [1, 2, 3]
        self.assertEqual([1, 2, 3, 5], ff(a=5, L=arr))

    def test_arbitrary_argument_list(self):
        self.assertEqual(10, sum_func(1, 2, 3, 4))
        self.assertEqual(10, sum_func(*[1, 2, 3, 4]),
                         "*로 list를 arguments로 unpacking")

    def test_dict_argument(self):
        self.assertEqual(10, sum_values(d1=1, d2=2, d3=3, d4=4))
        self.assertEqual(10, sum_values(**{"d1":1, "d2":2, "d3":3, "d4":4}),
                         "**로 dict을 arguments로 unpacking")

if __name__ == '__main__':
    unittest.main()
