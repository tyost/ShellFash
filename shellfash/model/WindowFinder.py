'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''

class WindowFinder(object):
    '''
    Finds native windows in the operating system.
    '''

    def __init__(self, _osWindowFinder = None):
        '''
        Constructor
        '''
        # Use the instance of the operating-system-specific WindowFinder
        # that was provided, if present.
        # Otherwise create one based on the operating system.
        if _osWindowFinder == None:
            from shellfash.model._WindowFinderWin32 import _WindowFinderWin32
            _osWindowFinder = _WindowFinderWin32()
            if not _osWindowFinder.is_supported():
                raise NotImplementedError(
                    'This platform is not supported.'
                )
        self._osWindowFinder = _osWindowFinder


    def get_visible_top_handles(self):
        '''
        Returns a list of all the visible and top-level window handles
        currently present on the system. 
        '''
        return self._osWindowFinder.get_visible_top_handles()
