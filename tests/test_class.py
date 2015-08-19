# -*- coding: utf-8 -*-
import unittest

class BaseClass:
    i = 1

    def __init__(self, var2):
        self.var = 5
        self.var2 = var2
        self.__private = "private"

    def f(self):
        return "BaseClass.f()"

class DerivedClass(BaseClass):
    def __init__(self):
        BaseClass.__init__(self, 2)

    def f(self):
        return "DerivedClass.f()"

class ReverseIter:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

class TestClass(unittest.TestCase):
    def test_class_attribute(self):
        inst = BaseClass(3)
        self.assertEqual(1, BaseClass.i)
        self.assertEqual(1, inst.i)
        BaseClass.i = 3
        self.assertEqual(3, BaseClass.i)
        self.assertEqual(3, inst.i)

    def test_data_attributes(self):
        inst = BaseClass(8)
        self.assertEqual(5, inst.var, "__init__는 instantiation operation")
        self.assertEqual(8, inst.var2)

        inst.new_var = 10
        self.assertEqual(10, inst.new_var, "data attributes를 추가할 수 있다")
        del inst.new_var
        with self.assertRaises(AttributeError):
            inst.new_var # 위에서 지웠기 때문에 접근 시 error

    def test_inheritance(self):
        d = DerivedClass()
        self.assertEqual(5, d.var)
        self.assertEqual(2, d.var2)
        self.assertTrue(isinstance(d, DerivedClass))
        self.assertTrue(isinstance(d, BaseClass))
        self.assertTrue(issubclass(d.__class__, BaseClass))

    def test_private_variables(self):
        d = BaseClass(10)
        self.assertEqual("private", d._BaseClass__private,
                         "__는 name mangling으로 _classname__member로 변경"
                         "access modifiers는 제공 안 하지만 이렇게 관례로 사용")

    def test_method_attributes(self):
        d = DerivedClass()
        self.assertTrue(hasattr(d.f, 'im_self'))
        self.assertTrue(hasattr(d.f, 'im_func'))

    def test_custom_iterator(self):
        self.assertEqual('dcba', ''.join(ReverseIter('abcd')))

    def test_custom_generator(self):
        def reverse_gen(data):
            for index in range(len(data)-1, -1, -1):
                yield data[index]

        self.assertEqual('dcba', ''.join(reverse_gen('abcd')))

if __name__ == '__main__':
    unittest.main()
