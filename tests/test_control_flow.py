# -*- coding: utf-8 -*-
import unittest

class TestControlFlow(unittest.TestCase):

    def test_elif(self):
        x = 1
        ret = False

        if x < 0:
            ret = False
        elif x == 1:
            ret = True

        self.assertTrue(ret, "elif가 else if")

    def test_range(self):
        self.assertEqual([0, 1, 2, 3, 4], range(5), "시작은 0이 디폴트")
        self.assertEqual([1, 2, 3, 4], range(1, 5), "step은 1이 디폴트")
        self.assertEqual([1, 3], range(1, 5, 2))

    def test_for(self):
        square = []
        for i in range(1, 4):
            square.append(i ** 2)

        self.assertEqual([1, 4, 9], square)

        num = range(2)
        for i in num[:]:
            num.insert(0, i)
        self.assertEqual([1, 0, 0, 1], num,
                         "루프를 도는 리스트를 변경해야 할 때는 [:]으로 복사본을 만들 것")

    def test_for_else(self):
        num = 10
        for i in range(1, 4):
            if i == 2:
                break
        else:
            num = i

        self.assertEqual(10, num, "break로 for문이 종료되면 else가 불리지 않는다")

        for i in range(1, 4):
            pass # noop.
        else:
            num = i

        self.assertEqual(3, num, "list를 모두 다 돌았을 때 호출함")

    def test_while_else(self):
        elseSet = False
        num = 1
        while num > 2:
            num += 1
        else:
            elseSet = True

        self.assertTrue(elseSet, "while 루프가 종료될 때도 호출")

if __name__ == '__main__':
    unittest.main()
