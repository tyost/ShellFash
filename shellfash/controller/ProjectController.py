'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from shellfash.framework import dependency
from shellfash.model.ProjectFolder import ProjectFolder
from shellfash.model.ProjectName import ProjectName


class ProjectController(object):
    '''
    Controls the model objects related to projects.
    '''

    @dependency.params(_clsProjectFolder=lambda: ProjectFolder)
    def __init__(self, _clsProjectFolder=None):
        '''
        Constructor.
        '''
        self._clsProjectFolder = _clsProjectFolder

    def create_project(self, projectNameString):
        '''
        Creates a project with the specified name.

        Args:
            projectNameString (string): The name of the project
                to create.

        Raises:
            OSError: If the project already exists or something else
                goes wrong with the file system.
            ProjectNameError: If the projectNameString is invalid.
        '''
        projectName = ProjectName(projectNameString)
        projectFolder = self._clsProjectFolder(projectName)
        projectFolder.create()

    def delete_project(self, projectNameString):
        '''
        Deletes a project with the specified name.

        Args:
            projectNameString (string): The name of the project
                to delete.

        Raises:
            OSError: If something goes wrong with the file system.
            ProjectNameError: If the projectNameString is invalid.
        '''
        projectName = ProjectName(projectNameString)
        projectFolder = self._clsProjectFolder(projectName)
        projectFolder.delete()
