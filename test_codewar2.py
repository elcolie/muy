import unittest

from codeware2 import main


class TestCodeWare2(unittest.TestCase):
    def test_readfile(self):
        ans = main()
        assert 0 != len(ans)
