'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import wx

class WindowPositionReader(object):
    '''
    Reads the position of native windows in the operating system.
    '''

    def __init__(self):
        '''
        Constructor
        '''


    def get_screen_position(self, handle):
        '''
        Returns a tuple containing the x and y coordinates, relative
            to the screen, of the window with the specified window handle.
            
        Args:
            handle (window handle): the handle of the window from which to read
                screen coordinates.
        '''
        wxWindow = wx.Window()
        wxWindow.AssociateHandle(handle)
        
        pointPosition = wxWindow.GetPosition()
        tuplePosition = pointPosition.Get()
        
        return tuplePosition
