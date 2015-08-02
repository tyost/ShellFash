'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.model.WindowFinder import WindowFinder
try:
    # Python 3.3 and higher.
    from unittest import mock
except ImportError:
    # Python 3.2.
    import mock

class Test(unittest.TestCase):
    '''
    Tests for WindowFinder.
    '''

    def setUp(self):
        # Set up doubles to replace real objects during testing.
        self.doubleOSWindowFinder = mock.NonCallableMock()
    
        # Create instance of class under test.
        self.windowFinder = WindowFinder(
            _osWindowFinder = self.doubleOSWindowFinder
        )


    def test__get_visible_top_handles__verify_return_is_from_osWindowFinder(self):
        self.doubleOSWindowFinder.get_visible_top_handles = (
                mock.Mock(return_value=['test']))
        returnValue = self.windowFinder.get_visible_top_handles()
        self.assertEqual(['test'], returnValue)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()