'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import time
import platform
if platform.system() == 'Linux':
    import xcffib
    from xcffib import xproto

class _TestWindowCreatorX11(object):
    '''
    Creates and cleans up windows to use for testing.
    '''

    def __init__(self, delay=0.05):
        '''
        Constructor
        
        Args:
            delay (Optional[float]): the extra time in seconds to wait for
                window creation or destruction.
        
        Attributes:
            windows (list): Holds references to the windows created
                for testing.
        '''
        self.windows = []
 
        self._delay = delay
        self._nextTitleNumber = 1


    def is_supported(self):
        '''
        Returns true if this object will work on this platform.
        '''
        return platform.system() == 'Linux'


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
        if len(self.windows):
            raise RuntimeError('Caught attempt to call create() a second '
                               'time without first calling destroy_all().')
        
        connection = xcffib.connect()
        setup = connection.get_setup()
        
        for _ in range(0, numWindows):
            handle = connection.generate_id()
            self.windows.append(handle)
            
            windowTitle = titleBase + str(self._nextTitleNumber)
            self._nextTitleNumber += 1
            
            connection.core.CreateWindow(
                depth = setup.roots[0].root_depth,
                wid = handle,
                parent = setup.roots[0].root,
                x = 0,
                y = 0,
                width = 640,
                height = 480,
                border_width = 0,
                _class = xproto.WindowClass.InputOutput,
                visual = setup.roots[0].root_visual,
                value_mask = 0,
                value_list = []
            )
            connection.core.ChangeProperty(
                mode = xproto.PropMode.Replace,
                window = handle,
                property = xcffib.xproto.Atom.WM_NAME,
                type = xcffib.xproto.Atom.STRING,
                format = 8,
                data_len = len(windowTitle),
                data = windowTitle
            )
            connection.core.MapWindow(handle)
            connection.flush()
        
        # Wait an extra delay in case the windows are actually not ready yet.
        time.sleep(self._delay)
        
    def destroy_all(self):
        '''
        Destroys all created windows.
        
        Does not reset the window title numbers.
        '''
        # Destroy each window.
        for handle in self.windows:
            connection = xcffib.connect()
            connection.core.DestroyWindow(
                window = handle
            )
            connection.flush()
        
        # Empty the public list of windows.
        self.windows.clear()
        
        # Wait an extra delay in case the windows are not destroyed yet.
        time.sleep(self._delay)

    def get_handle(self, index):
        '''
        Returns the numeric handle for the native window.
        
        Args:
            index (int): the index of the window in the window attribute
                whose handle will be returned.
        '''
        return self.windows[index]
    
    def get_screen_position(self, index):
        '''
        Returns a tuple containing the x and y screen coordinates
            for the native window.
        
        Args:
            index (int): the index of the window in the window attribute
                whose screen position will be returned.
        '''
        return (
            -42,
            -42
        )
