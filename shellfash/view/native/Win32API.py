'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import ctypes
import ctypes.wintypes

class Win32API(object):
    '''
    Wraps parts of the Microsoft Windows API that are needed.
    '''

    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    
    # Constants for parameter dwStyle in CreateWindowEx.
    WS_BORDER = 0x00800000
    WS_CAPTION = 0x00C00000
    WS_CHILD = 0x40000000
    WS_CHILDWINDOW = 0x40000000
    WS_CLIPCHILDREN = 0x02000000
    WS_CLIPSIBLINGS = 0x04000000
    WS_DISABLED = 0x08000000
    WS_DLGFRAME = 0x00400000
    WS_GROUP = 0x00020000
    WS_HSCROLL = 0x00100000
    WS_ICONIC = 0x20000000
    WS_MAXIMIZE = 0x01000000
    WS_MAXIMIZEBOX = 0x00010000
    WS_MINIMIZE = 0x20000000
    WS_MINIMIZEBOX = 0x00020000
    WS_OVERLAPPED = 0x00000000
    WS_POPUP = 0x80000000
    WS_SIZEBOX = 0x00040000
    WS_SYSMENU = 0x00080000
    WS_TABSTOP = 0x00010000
    WS_THICKFRAME = 0x00040000
    WS_TILED = 0x00000000
    WS_VISIBLE = 0x10000000
    WS_VSCROLL = 0x00200000
    WS_OVERLAPPEDWINDOW = (WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU |
                           WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX)
    WS_POPUPWINDOW = WS_POPUP | WS_BORDER | WS_SYSMENU
    WS_TILEDWINDOW = (WS_OVERLAPPED | WS_CAPTION | WS_SYSMENU |
                      WS_THICKFRAME | WS_MINIMIZEBOX | WS_MAXIMIZEBOX)
    
    
    def CreateWindowEx( self,
                        dwExStyle,
                        lpClassName,
                        lpWindowName,
                        dwStyle,
                        x,
                        y,
                        nWidth,
                        nHeight,
                        hWndParent = None,
                        hMenu = None,
                        hInstance = None,
                        lpParam = None
                     ):
        '''
        See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms632680%28v=vs.85%29.aspx
        '''
        # Create a reference to the real wrapper from ctypes
        # if we don't have one already.
        if not hasattr(Win32API, '_CreateWindowEx'):
            # Note: We are using the version with W
            # on the end which has Unicode support.
            Win32API._CreateWindowEx = ctypes.windll.user32.CreateWindowExW
            Win32API._CreateWindowEx.argtypes = [
                ctypes.wintypes.DWORD,
                ctypes.wintypes.LPCWSTR,
                ctypes.wintypes.LPCWSTR,
                ctypes.wintypes.DWORD,
                ctypes.wintypes.INT,
                ctypes.wintypes.INT,
                ctypes.wintypes.INT,
                ctypes.wintypes.INT,
                ctypes.wintypes.HWND,
                ctypes.wintypes.HMENU,
                ctypes.wintypes.HINSTANCE,
                ctypes.wintypes.LPVOID
            ]
            Win32API._CreateWindowEx.restype = ctypes.wintypes.HWND
            
        return Win32API._CreateWindowEx(
            dwExStyle,
            lpClassName,
            lpWindowName,
            dwStyle,
            x,
            y,
            nWidth,
            nHeight,
            hWndParent,
            hMenu,
            hInstance,
            lpParam
        )
    
    def DestroyWindow(self, hWnd):
        '''
        See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms632682%28v=vs.85%29.aspx
        '''
        # Create a reference to the real wrapper from ctypes
        # if we don't have one already.
        if not hasattr(Win32API, '_DestroyWindow'):
            Win32API._DestroyWindow = ctypes.windll.user32.DestroyWindow
            Win32API._DestroyWindow.argtypes = [ctypes.wintypes.HWND]
            Win32API._DestroyWindow.restype = ctypes.wintypes.BOOL
        
        return bool(Win32API._DestroyWindow(hWnd))
    
    def GetModuleHandle(self, lpModuleName = None):
        '''
        See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms683199%28v=vs.85%29.aspx
        '''
        # Create a reference to the real wrapper from ctypes
        # if we don't have one already.
        if not hasattr(Win32API, '_GetModuleHandle'):
            Win32API._GetModuleHandle = ctypes.windll.kernel32.GetModuleHandleW
            Win32API._GetModuleHandle.argtypes = [ctypes.wintypes.LPCWSTR]
            Win32API._GetModuleHandle.restype = ctypes.wintypes.HMODULE
        
        return Win32API._GetModuleHandle(lpModuleName)
    
    def IsIconic(self, hWnd):
        '''
        See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms633527%28v=vs.85%29.aspx
        '''
        # Create a reference to the real wrapper from ctypes
        # if we don't have one already.
        if not hasattr(Win32API, '_IsIconic'):
            Win32API._IsIconic = ctypes.windll.user32.IsIconic
            Win32API._IsIconic.argtypes = [ctypes.wintypes.HWND]
            Win32API._IsIconic.restype = ctypes.wintypes.BOOL
        
        return bool(Win32API._IsIconic(hWnd))
    
    # Constants for parameter nCmdShow in ShowWindow and ShowWindowAsync.
    SW_FORCEMINIMIZE = 11
    SW_HIDE = 0
    SW_MAXIMIZE = 3
    SW_MINIMIZE = 6
    SW_RESTORE = 9
    SW_SHOW = 5
    SW_SHOWDEFAULT = 10
    SW_SHOWMAXIMIZED = 3
    SW_SHOWMINIMIZED = 2
    SW_SHOWMINNOACTIVE = 7
    SW_SHOWNA = 8
    SW_SHOWNOACTIVATE = 4
    SW_SHOWNORMAL = 1
    
    def ShowWindow(self, hWnd, nCmdShow):
        '''
        See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms633548%28v=vs.85%29.aspx
        '''
        # Create a reference to the real wrapper from ctypes
        # if we don't have one already.
        if not hasattr(Win32API, '_ShowWindow'):
            Win32API._ShowWindow = ctypes.windll.user32.ShowWindow
            Win32API._ShowWindow.argtypes = [
                ctypes.wintypes.HWND,
                ctypes.wintypes.INT
            ]
            Win32API._ShowWindow.restype = ctypes.wintypes.BOOL
        
        return bool(Win32API._ShowWindow(hWnd, nCmdShow))
    
    def ShowWindowAsync(self, hWnd, nCmdShow):
        '''
        See: https://msdn.microsoft.com/en-us/library/windows/desktop/ms633549%28v=vs.85%29.aspx
        '''
        # Create a reference to the real wrapper from ctypes
        # if we don't have one already.
        if not hasattr(Win32API, '_ShowWindowAsync'):
            Win32API._ShowWindowAsync = ctypes.windll.user32.ShowWindowAsync
            Win32API._ShowWindowAsync.argtypes = [
                ctypes.wintypes.HWND,
                ctypes.wintypes.INT
            ]
            Win32API._ShowWindowAsync.restype = ctypes.wintypes.BOOL
        
        return bool(Win32API._ShowWindowAsync(hWnd, nCmdShow))
