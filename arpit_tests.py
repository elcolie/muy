import unittest

from iksan import answer


class TestStringMethods(unittest.TestCase):

    def test_normal(self):
        question = ['3', '-2']
        assert -2 == answer(question)

    def test_some_duplication(self):
        question = ['5', '5', '4', '2']
        assert 4 == answer(question)

    def test_full_duplication(self):
        question = ['4', '4', '4']
        assert -1 == answer(question)

    def test_blank_array(self):
        assert -1 == answer([])

    def test_double_duplication(self):
        question = ['7', '7', '5', '5', '4', '2']
        assert 5 == answer(question)

    def test_null(self):
        question = None
        assert -1 == answer(question)


if __name__ == '__main__':
    unittest.main()
