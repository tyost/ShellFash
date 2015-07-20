'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.model.ProjectNameError import ProjectNameError

class ProjectName(object):
    '''
    Represents the valid name of a project.
    '''

    def __init__(self,
                 projectNameString,
                 _nameValidator = None):
        '''
        Constructor.
        
        Args:
            projectNameString (string): The project name to use.
        '''
        # Create default dependencies, if needed.
        if _nameValidator == None:
            from shellfash.model.ProjectNameValidator \
                    import ProjectNameValidator
            _nameValidator = ProjectNameValidator()
        
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
