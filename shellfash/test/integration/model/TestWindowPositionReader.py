'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.test.helper.TestWindowCreator import TestWindowCreator
from shellfash.model.WindowPositionReader import WindowPositionReader

@unittest.skip(
    'These tests are not working properly. They are hanging on Debian Linux.'
)
class TestWindowPositionReader(unittest.TestCase):
    '''
    Tests for WindowPositionReader.
    '''

    def setUp(self):
        self.windowCreator = TestWindowCreator()
        self.reader = WindowPositionReader()
    
    def tearDown(self):
        self.windowCreator.destroy_all()


    def test__get_screen_position__returns_tuple(self):
        self.windowCreator.create('test_get_screen_position_returns_tuple', 1)
        handle = self.windowCreator.windows[0].winfo_id()
        self.assertIsInstance(
            obj = self.reader.get_screen_position(handle),
            cls = tuple
        )
        
    def test__get_screen_position__returns_window_coordinates(self):
        self.windowCreator.create('test_get_screen_position_returns_coords', 1)
        self.windowCreator.windows[0].geometry('+17+17')
        
        handle = self.windowCreator.get_handle(0)
        expectedPosition = self.windowCreator.get_screen_position(0)
        self.assertTupleEqual(
            tuple1 = expectedPosition,
            tuple2 = self.reader.get_screen_position(handle)
        )


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()