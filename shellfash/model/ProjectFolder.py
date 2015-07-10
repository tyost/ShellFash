'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import os

class ProjectFolder(object):
    '''
    Opens files in a project's folder.
    '''

    def __init__(self,
                 projectName,
                 _appDirs=None,
                 _nameValidator=None,
                 _open=open):
        '''
        Constructor
        
        Args:
            projectName (string): The name of the project.
            
        Raises:
            ValueError: If projectName does not fit the syntax for
                the name of a project.
        '''
        
        if not _nameValidator:
            from shellfash.model.ProjectNameValidator \
                    import ProjectNameValidator
            self._nameValidator = ProjectNameValidator()
        else:
            self._nameValidator = _nameValidator

        if not _nameValidator.validate(projectName):
            raise ValueError('Argument projectName was "' + projectName
                             + '" which does not match the syntax'
                             'for a valid project name.')
        else:
            self._projectName = projectName 
        
        if not _appDirs:
            from appdirs import AppDirs
            self._appDirs = AppDirs(appname = 'shellfash')
        else:
            self._appDirs = _appDirs
    
        self._open = _open
    
    
    def get_base_path(self):
        '''
        Returns a string giving the base path to the folder
            for ShellFash projects. The returned string does not
            end in a directory separator (slash).
        '''
        
        # TODO: Read path from config.ini if present
        # (using a separate class like GlobalConfig).
        # Otherwise get the path from appdirs.
        return self._appDirs.user_data_dir()
    
    def get_path(self):
        '''
        Returns a string giving the path to the folder for this
            ShellFash project. The returned string does not end
            in a directory separator (slash).
        '''
        
        return os.path.join(
            self.get_base_path(),
            self._projectName
        )
    
    def join(self, *args):
        '''
        Builds a file path from the passed arguments, starting
            with the path for the project's folder.
        
        Args:
            *args (strings): The parts of the path.
            
        Returns:
            string: The combined path.
        '''
        
        return os.path.join(self.get_path(), *args)
    
    def join_open(self, pathSequence, *args, **kwargs):
        '''
        Opens
        '''
        
        return self._open(self.join(*pathSequence), *args, **kwargs)
