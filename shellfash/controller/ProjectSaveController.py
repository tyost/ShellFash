'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''

class ProjectSaveController(object):
    '''
    Saves visible windows to a project.
    '''

    def __init__(self,
                 _windowSaver=None):
        '''
        Constructor.
        '''
        if _windowSaver == None:
            from shellfash.model.ProjectWindowSaver import ProjectWindowSaver
            _windowSaver = ProjectWindowSaver()
        self._windowSaver = _windowSaver


    def saveall(self, projectName):
        '''
        Constructor.
        
        Args:
            projectName (ProjectName): The object giving the name
                of the project.
        '''
        self._windowSaver.save_visible(projectName)
