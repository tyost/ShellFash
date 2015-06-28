'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from threading import Barrier, Thread
import wx
import time

class TestWindowCreator(object):
    '''
    Creates and cleans up windows to use for testing.
    '''

    def __init__(self):
        '''
        Constructor
        
        Attributes:
            windows (list): Holds references to the Frames from wxPython
                created for testing.
        '''
        self.windows = []
        
        self._syncBarrier = Barrier(2, timeout = 5)
        self._nextTitleNumber = 1
        self._wxApp = None
        self._wxThread = None
    
    
    def create(self, titleBase = 'TestWindow', numWindows = 1):
        '''
        Creates operating system windows (Frames in wxPython).
        Adds them to the list in the public 'windows' property.
        
        Every calls to create() should eventually end in a call to
        destroy_all(). This method cannot be called twice without
        a call to destroy_all() after the first call.
        
        Args:
            titleBase (Optional[str]): The left part of the created
                window titles. A number is added to the end (right)
                of the base title. Default is "TestWindow".
            numWindows (Optional[int]): The number of windows to create.
                Default is 1.
                
        Raises:
            RuntimeError: If two calls are made to create() without
                a destroy_all() call between them.
        '''
        
        if self._wxApp:
            raise RuntimeError('Caught attempt to call create() a second '
                               'time without first calling destroy_all().')
        
        self._wxApp = wx.App(False)
        
        # Create the windows (Frames) and add them to the public
        # windows list.
        for i in range(0, numWindows):
            windowTitle = titleBase + str(self._nextTitleNumber)
            self.windows.append(
                wx.Frame(None, wx.ID_ANY, windowTitle)
            )
            self.windows[i].Show()
            self._nextTitleNumber += 1
        
        # Run the wxPython main loop in a different thread.
        # One reason is that it loops indefinitely and would block
        # other code from running in the main thread.
        def wx_creation_thread_target():
            nonlocal self
            self._wxApp.MainLoop()
            
        # Start the wxPython thread as a daemon so it should exit
        # even if the main thread unexpectedly exits first.
        self._wxThread = Thread(
            target = wx_creation_thread_target,
            daemon = True
        )
        self._wxThread.start()
        
        # _Thread synchronization 1_
        # Make sure the wxPython thread waits in the barrier after
        # processing the window (Frame) creation.
        wx.CallAfter(self._syncBarrier.wait)
        # Make sure this main thread waits in the barrier until the
        # wxPython thread is finished with the window (Frame) creation.
        self._syncBarrier.wait()
        
        # We synchronized at the barrier. Reset the barrier for next time.
        self._syncBarrier.reset()
        
    def destroy_all(self):
        '''
        Destroys all created windows (wxPython Frames) and the wxPython
            App object.
        
        Does not reset the window title numbers.
        
        Note: As of 2015-6, this method doesn't actually work correctly.
            The spawned wxPython threads and windows only die when
            the main thread dies.
        '''       
        
        # Destroy the windows (Frames) in the wxPython thread.
        for window in self.windows:
            window.Destroy()

        wx.Exit()
        # We need some way to wake up the wxPython thread and tell it
        # to die, but an easy way does not seem to exist yet.
        #wx.WakeUpMainThread()

        # Empty the public list of windows.
        self.windows.clear()
        
        # Mark the wxPython App and thread as killed.
        self._wxApp = None
        self._wxThread = None
