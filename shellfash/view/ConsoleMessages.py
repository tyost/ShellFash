'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.model.ProjectFolder import ProjectFolder
from shellfash.model.ProjectName import ProjectName


class ConsoleMessages(object):
    '''
    Generates the messages to display in the console.
    '''

    def __init__(self):
        '''
        Constructor.
        '''
        pass

    def get_project_created(self, projectNameString):
        '''
        Returns the message to display when a project is created
        successfully.

        Args:
            projectNameString (string): The name of the project
                to use in the message.

        Returns:
            string: The message using projectNameString.
        '''
        return "Project '%s' created." % projectNameString
