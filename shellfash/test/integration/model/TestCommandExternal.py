'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import platform
import unittest

from shellfash.model.CommandExternal import CommandExternal


class TestCommandExternal(unittest.TestCase):
    '''
    Integration tests for CommandExternal.
    '''

    def setUp(self):
        pass

    @unittest.skipUnless(
        platform.system() == 'Linux',
        'This test only works on a Unix-like platform.'
    )
    def test__run__linux_ls_returns_success_exit_code(self):
        command = CommandExternal('ls')
        self.assertEqual(0, command.run())


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
