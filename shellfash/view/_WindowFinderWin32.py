'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import platform

class _WindowFinderWin32(object):
    '''
    Finds native windows in the Microsoft Windows operating system.
    
    Use WindowFinder instead of using this class directly.
    '''
    
    def __init__(self, _win32=None):
        '''
        Constructor
        '''
        if _win32 == None:
            from shellfash.view.native.Win32API import Win32API
            _win32 = Win32API()
        self._win32 = _win32


    def is_supported(self):
        '''
        Returns true if this object will work on this platform.
        '''
        return platform.system() == 'Windows'

    def get_visible_top_handles(self):
        '''
        Returns a list of all the visible and top-level window handles
        currently present on the system. 
        '''
        handleList = []
        
        def EnumWindowsCallback(hWnd, lParam):
            if self._win32.IsWindowVisible(hWnd):
                handleList.append(hWnd)
            return True
        
        self._win32.EnumWindows(
            lpEnumFunc = EnumWindowsCallback,
            lParam = 0
        )
        
        return handleList
