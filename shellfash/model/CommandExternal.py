'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import subprocess

from shellfash.framework import dependency


class CommandExternal(object):
    '''
    Represents an arbitrary command-line statement to ask the operating system
        to execute.
    '''

    @dependency.params(_subprocess=lambda: subprocess)
    def __init__(self,
                 commandString,
                 _subprocess=None):
        '''
        Constructor.

        Args:
            commandString (string): The command to send
                to the operating system. For example: 'ls'.
        '''
        self._commandString = commandString
        self._subprocess = _subprocess

    def run(self):
        '''
        Asks the operating system to execute the command in this
        object. Returns when the command finishes.

        Returns:
            int: The exit code from the executed command.
        '''
        return self._subprocess.call(self._commandString)
