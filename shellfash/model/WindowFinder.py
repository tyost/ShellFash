'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.model._WindowFinderWin32 import _WindowFinderWin32  # @UnusedImport
from shellfash.model._WindowFinderX11 import _WindowFinderX11  # @UnusedImport

_NATIVE_CLASS_NAMES = (
    '_WindowFinderWin32',
    '_WindowFinderX11'
)

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
            global _NATIVE_CLASS_NAMES
            
            for className in _NATIVE_CLASS_NAMES:
                tempOSWindowFinder = globals()[className]()
                if tempOSWindowFinder.is_supported():
                    _osWindowFinder = tempOSWindowFinder
        
        if _osWindowFinder == None:
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
