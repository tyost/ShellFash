'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.framework import dependency
from shellfash.model.ProjectNameError import ProjectNameError
from shellfash.model.ProjectNameValidator import ProjectNameValidator


class ProjectName(object):
    '''
    Represents the valid name of a project.
    '''

    @dependency.params(_nameValidator=ProjectNameValidator)
    def __init__(self,
                 projectNameString,
                 _nameValidator=None):
        '''
        Constructor.

        Args:
            projectNameString (string): The project name to use.
        '''
        # Validate projectNameString.
        if not _nameValidator.validate(projectNameString):
            raise ProjectNameError(
                'projectNameString must be a valid name for a project, '
                "but it was: '{}'".format(projectNameString)
            )

        self._projectNameString = projectNameString

    def get_full_name(self):
        '''
        Returns the full project name.
        '''
        return self._projectNameString
