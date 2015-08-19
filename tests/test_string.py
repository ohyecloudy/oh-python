# -*- coding: utf-8 -*-
import unittest

class TestStringMethods(unittest.TestCase):

    def test_quotes(self):
        self.assertEqual("string", 'string',
                         "double quotes와 single quotes 결과는 같다")
        self.assertEqual("'string'", '\'string\'',
                         "double quotes 안에 single quotes는 그대로 사용")

    def test_raw_string(self):
        self.assertEqual("c:\\temp\\temp1", r"c:\temp\temp1",
                         "r prefix를 사용해 raw string을 사용할 수 있다.")

    def test_concatenate(self):
        self.assertEqual("unununium", 3 * 'un' + "ium",
                         "*, + operator 사용가능")
        self.assertEqual("python", "py" "thon",
                         "string literal은 자동으로 이어준다")

    def test_indexed(self):
        word = 'python'
        self.assertEqual('p', word[0], "당연히 0부터 시작")
        self.assertEqual('n', word[5])
        with self.assertRaises(IndexError):
            self.assertEqual('n', word[6], "index를 벗어나면 IndexError 발생")
        self.assertEqual('n', word[-1], "-1은 last character")
        self.assertEqual('p', word[-6])
        with self.assertRaises(IndexError):
            self.assertEqual('p', word[-7])

    def test_slicing(self):
        word = 'python'
        self.assertEqual('py', word[0:2], "[0,2)")
        self.assertEqual('py', word[:2], "0이 디폴트")
        self.assertEqual('on', word[4:], "end가 디폴트")
        self.assertEqual('python', word[:2] + word[2:])
        self.assertEqual('on', word[-2:], "-도 오키")

    def test_out_of_range_slicing(self):
        word = 'python'
        with self.assertRaises(IndexError):
            word[42]
        self.assertEqual('on', word[4:42], 'out of range를 알아서 처리')
        self.assertEqual('', word[42:], 'out of range를 알아서 처리')

    def test_immutable(self):
        word = 'python'
        with self.assertRaises(TypeError):
            word[0] = 'j'

    def test_len(self):
        word = 'python'
        self.assertEqual(6, len(word), "문자열 길이 구하는 함수는 built-in")

if __name__ == '__main__':
    unittest.main()
