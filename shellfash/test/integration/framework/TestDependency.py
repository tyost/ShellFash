import unittest
from shellfash.framework import dependency


class TestDependency(unittest.TestCase):
    '''
    Integration tests for module 'dependency'.
    '''

    def test__params__injects_number(self):
        @dependency.params(number=lambda: 42)
        def test(number=None):
            return number
        self.assertEqual(42, test())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
