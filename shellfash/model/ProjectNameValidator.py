'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import re

class ProjectNameValidator(object):
    '''
    Checks if project names are valid.
    
    A name is valid if it:
        starts with a number, letter or underscore,
        contains only numbers, letters, underscores, spaces, dots or hyphens,
        and ends with a number, letter, or underscore.
    '''

    def __init__(self):
        '''
        Constructor.
        '''
        self._regex = re.compile(
            r'^[a-zA-Z0-9_]$'
            r'|'
            r'^[a-zA-Z0-9_]'
            r'[a-zA-Z0-9_ .-]*'
            r'[a-zA-Z0-9_]$'
        )
    
    
    def validate(self, projectName):
        '''
        Returns True if a project name is valid.
        
        Args:
            projectName (string): The project name to check.
            
        Returns:
            bool: True if projectName is valid, False otherwise.
        '''
        return bool(self._regex.match(projectName))
