'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''

from shellfash.test.helper._TestWindowCreatorWin32 import _TestWindowCreatorWin32  # @UnusedImport
from shellfash.test.helper._TestWindowCreatorX11 import _TestWindowCreatorX11  # @UnusedImport

_NATIVE_CLASS_NAMES = (
    '_TestWindowCreatorWin32',
    '_TestWindowCreatorX11'
)

class TestWindowCreator(object):
    '''
    Creates and cleans up windows to use for testing.
    '''

    def __init__(self, delay=0.05, _osWindowCreator=None):
        '''
        Constructor
        
        Args:
            delay (Optional[float]): the extra time in seconds to wait for
                window creation or destruction.
        
        Attributes:
            windows (list): Holds references to the windows created
                for testing.
        '''
        # Use the instance of the operating-system-specific TestWindowCreator
        # that was provided, if present.
        # Otherwise create one based on the operating system.
        if _osWindowCreator == None:
            global _NATIVE_CLASS_NAMES
            
            for className in _NATIVE_CLASS_NAMES:
                tempOSWindowCreator = globals()[className](delay)
                if tempOSWindowCreator.is_supported():
                    _osWindowCreator = tempOSWindowCreator
        
        if _osWindowCreator == None:
            raise NotImplementedError(
                'This platform is not supported.'
            )
        self._osWindowCreator = _osWindowCreator
        
        # TODO: getter property 'windows'

    def create(self, titleBase = 'TestWindow', numWindows = 1):
        '''
        Creates operating system windows.
        Adds them to the list in the public 'windows' property.
        
        Every call to create() should eventually end in a call to
        destroy_all(). This method cannot be called twice without
        a call to destroy_all() after the first call.
        
        Args:
            titleBase (Optional[str]): The left part of the created
                window titles. A number is added to the end (right)
                of the base title. Default is "TestWindow".
            numWindows (Optional[int]): The number of windows to create.
                Default is 1.
        '''
        self._osWindowCreator.create(titleBase, numWindows)
        
    def destroy_all(self):
        '''
        Destroys all created windows.
        
        Does not reset the window title numbers.
        '''       
        self._osWindowCreator.destroy_all()

    def get_handle(self, index):
        '''
        Returns the numeric handle for the native window.
        
        Args:
            index (int): the index of the window in the window attribute
                whose handle will be returned.
        '''
        self._osWindowCreator.get_handle(index)
    
    def get_screen_position(self, index):
        '''
        Returns a tuple containing the x and y screen coordinates
            for the native window.
        
        Args:
            index (int): the index of the window in the window attribute
                whose screen position will be returned.
        '''
        self._osWindowCreator.get_screen_position(index)
