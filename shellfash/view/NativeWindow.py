'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.view._NativeWindowWin32 import _NativeWindowWin32

class NativeWindow(object):
    '''
    Class representing a native window in the operating system.

    Performs actions on native windows that are not explicitly built
    into Python or other cross-platform libraries that could be found.
    '''

    def __init__(self, windowHandle, _clsNativeWindow = None):
        '''
        Constructor.
        
        Args:
            windowHandle (int or wxWindow): The number representing
                a native window from the operating system. It can also
                be an object with a getHandle method, such as a wxPython
                Window object.
        '''        
        # Use the windowHandle itself if it can be converted to an integer.
        try:
            self._handle = int(windowHandle)
        except (AttributeError, TypeError, ValueError):
            pass
        
        # Try to pull the windowHandle from the getHandle() method.
        try:
            self._handle = int(windowHandle.getHandle())
        except (AttributeError, TypeError, ValueError):
            pass
        
        # Throw an exception if no valid window handle could be found.
        if not hasattr(self, '_handle'):
            raise TypeError('Argument windowHandle must be an integer '
                            'or have a getHandle function returning one.')
        
        # Create a new instance of the native window class
        # that was provided, if possible.
        try:
            _osNativeWindow = _clsNativeWindow(self._handle)
            if _osNativeWindow.is_supported():
                self._osNativeWindow = _osNativeWindow
        except (AttributeError, TypeError, ValueError):
            pass
        
        # Otherwise create one based on the operating system.
        if not hasattr(self, '_osNativeWindow'):
            self._osNativeWindow = _NativeWindowWin32(self._handle)
            if not self._osNativeWindow.is_supported():
                raise NotImplementedError(
                    'This platform is not supported.'
                )
    
    def get_handle(self):
        '''
        Returns the number representing a native window from the operating
        system.
        '''
        return self._handle
    
    def is_minimized(self):
        '''
        Returns true if the window is minimized.
        '''
        return self._osNativeWindow.is_minimized()
    
    def set_minimized(self, minimize, waitForAnimation = False):
        '''
        Minimizes or restores the window from being minimized.
        
        Args:
            minimize (boolean): If true and the window is not
                minimized, minimize the window. If false and
                the window is minimized, restore the window.
            waitForAnimation (boolean): If true, wait for the
                animation to play before returning.
        '''
        if (minimize and not self.is_minimized()) \
                or (not minimize and self.is_minimized()):
            self._osNativeWindow.set_minimized(minimize, waitForAnimation)
