'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import platform
from shellfash.view.native.Win32API import Win32API

class _NativeWindowWin32(object):
    '''
    Class representing a native window in the Microsoft Windows
    operating system.
    
    Use NativeWindow instead of using this class directly.

    Performs actions on native windows that are not explicitly built
    into Python or other cross-platform libraries that could be found.
    '''

    def __init__(self, windowHandle, _win32=None):
        '''
        Constructor
        '''
        self._handle = windowHandle
        self._win32 = _win32 or Win32API()
    
    
    def is_supported(self):
        '''
        Returns true if this object will work on this platform.
        '''
        return platform.system() == 'Windows'
    
    def is_minimized(self):
        '''
        Returns true if the window is minimized.
        '''
        
        # TOOD: We can detect SW_MINIMIZE with IsIconic(), but how do we
        # detect SW_FORCEMINIMIZE?
        
        raise NotImplementedError()
    
    def set_minimized(self, minimize, waitForAnimation = False):
        '''
        Minimizes or restores the window from being minimized.
        
        Args:
            minimize (boolean): If true, minimize the window.
                If false and the window is minimized, restore the window.
            waitForAnimation (boolean): If true, wait for the
                animation to play before returning.
        '''
        if minimize:
            nCmdShow = self._win32.ShowWindow.SW_MINIMIZE
            
            # TODO: Force minimize if the minimize didn't take?
            
        else:
            nCmdShow = self._win32.ShowWindow.SW_RESTORE
         
        if waitForAnimation:
            self._win32.ShowWindow(self._handle, nCmdShow)
        else:
            self._win32.ShowWindowAsync(self._handle, nCmdShow)
