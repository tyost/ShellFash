'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import platform
if platform.system() == 'Linux':
    import xcffib
    from xcffib import xproto

class _WindowFinderX11(object):
    '''
    Finds native windows in the Microsoft Windows operating system.
    
    Use WindowFinder instead of using this class directly.
    '''
    
    def __init__(self):
        '''
        Constructor
        '''
        pass


    def is_supported(self):
        '''
        Returns true if this object will work on this platform.
        '''
        return platform.system() == 'Linux'

    def get_visible_top_handles(self):
        '''
        Returns a list of all the visible and top-level window handles
        currently present on the system. 
        '''
        handleList = []
        
        connection = xcffib.connect()
        
        return handleList
