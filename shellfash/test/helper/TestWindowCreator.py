'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from tkinter import Tk, Toplevel
from threading import Barrier, Thread
import time

class TestWindowCreator(object):
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
        self._syncBarrier = Barrier(2, timeout = 1)
        self._tkApp = None
        self._tkThread = None


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
        if self._tkApp:
            raise RuntimeError('Caught attempt to call create() a second '
                               'time without first calling destroy_all().')
        
        # Run the Tk main loop in a different thread.
        # One reason is that it loops indefinitely and would block
        # other code from running in the main thread.
        def tk_thread_function():
            # Create the top-most window for Tk that kind of serves
            # as the "app", since we start the event loop from it.
            # It also serves as the first window we create.
            self._tkApp = Tk()
            self.windows.append(self._tkApp)
            windowTitle = titleBase + str(self._nextTitleNumber)
            self._tkApp.wm_title(windowTitle)
            self._nextTitleNumber += 1
        
            # Create extra windows beyond the first and add them
            # to the public windows list.
            for i in range(1, numWindows):
                self.windows.append(
                    Toplevel(self._tkApp)
                )
                windowTitle = titleBase + str(self._nextTitleNumber)
                self.windows[i].wm_title(windowTitle)
                self._nextTitleNumber += 1
            
            # _Thread synchronization 1_
            # Make sure the Tk thread waits in the barrier after
            # processing the window creation.
            self._tkApp.after(0, self._syncBarrier.wait)
            
            # Start the endless window event loop.
            self._tkApp.mainloop()
            
            # _Thread synchronization 2_
            self._syncBarrier.wait()
        
        # Start the Tk thread as a daemon so it should exit
        # even if the main thread unexpectedly exits first.
        self._tkThread = Thread(
            target = tk_thread_function,
            daemon = True
        )
        self._tkThread.start()

        # _Thread synchronization 1_
        # Make sure this main thread waits in the barrier until the
        # Tk thread is finished with the window creation.
        self._syncBarrier.wait()
        # We synchronized at the barrier. Reset the barrier for next time.
        self._syncBarrier.reset()
        
        # Wait an extra delay in case the windows are actually not ready yet.
        time.sleep(self._delay)
        
    def destroy_all(self):
        '''
        Destroys all created windows.
        
        Does not reset the window title numbers.
        '''       
        # Destroy the Tk App and its windows.
        if self._tkApp:
            self._tkApp.after(0, self._tkApp.quit)

        # _Thread synchronization 2_
        # Make sure this main thread waits in the barrier until the
        # Tk thread is finished closing the windows.
        self._syncBarrier.wait()
        # We synchronized at the barrier. Reset the barrier for next time.
        self._syncBarrier.reset()

        # Empty the public list of windows.
        self.windows.clear()
        
        # Mark the Tk App and thread as killed.
        self._tkApp = None
        self._tkThread = None
        
        # Wait an extra delay in case the windows are not destroyed yet.
        time.sleep(self._delay)

    def get_handle(self, index):
        '''
        Returns the numeric handle for the native window.
        
        Args:
            index (int): the index of the window in the window attribute
                whose handle will be returned.
        '''
        return int(self.windows[index].frame(), 16)
    
    def get_screen_position(self, index):
        '''
        Returns a tuple containing the x and y screen coordinates
            for the native window.
        
        Args:
            index (int): the index of the window in the window attribute
                whose screen position will be returned.
        '''
        return (
            self.windows[index].winfo_x(),
            self.windows[index].winfo_y()
        )
