'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''

# Not extending ValueError to avoid getting caught
# up in try/catches for other ValueError reasons.
class ProjectNameError(Exception):
    '''
    Indicates a problem creating a ProjectName from a particular string.
    '''
