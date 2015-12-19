'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.framework import dependency


class CommandRunner(object):
    '''
    Runs multiple command objects.
    '''

    def __init__(self):
        '''
        Constructor.
        '''
        self._commands = []

    def add(self, command):
        '''
        Add a command object to the end of the commands to run.

        Args:
            command: The command object to add.
        '''
        self._commands.append(command)

    def runAll(self):
        '''
        Run all commands in the order they were added to this runner.
        '''
        for command in self._commands:
            command.run()
