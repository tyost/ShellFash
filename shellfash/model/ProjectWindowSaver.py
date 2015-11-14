'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''

class ProjectWindowSaver(object):
    '''
    Saves window information to the file system for a project.
    '''

    def __init__(self,
                 _windowFinder=None):
        '''
        Constructor.
        '''
        if _windowFinder == None:
            from shellfash.model.WindowFinder import WindowFinder
            _windowFinder = WindowFinder()
        self._windowFinder = _windowFinder


    def save_visible(self, projectName):
        '''
        Saves visible windows to the specified project name.
        
        Args:
            projectName (ProjectName): The object giving the name
                of the project.
        '''
        # TODO: Factor out a new class to hold the window information
        # to be saved to disk.
        self._windowFinder.get_visible_top_handles()
