'''
ShellFash command line

License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import click

from shellfash.controller.ProjectController import ProjectController
from shellfash.model.ProjectFolder import ProjectFolder
from shellfash.model.ProjectName import ProjectName


def _setDependencies(projectController=None):
    '''
    Put dependencies in module-level variables to permit using
    test doubles.
    '''
    if projectController == None:
        projectController = ProjectController()

    global _projectController
    _projectController = projectController

_setDependencies()


@click.group()
def main():
    '''
    ShellFash is a program to quickly save and restore your progress
    on a particular computer project. Your progress includes running
    programs and their window positions.
    '''
    # TODO: Somewhere we need exception handling for failed imports
    # of required libraries. We want to show a user-friendly message
    # about what library is missing and how to get it.


# See http://www.gnu.org/prep/standards/html_node/Option-Table.html#Option-Table
# for command option standards.


# TODO: A command to move the existing folders to a new location and change
# the setting for where folders are located?
def folder():
    pass


@main.command()
@click.argument('name')
def new(name):
    '''
    Creates a new project with the specified NAME.
    '''
    _projectController.create_project(name)
    click.echo('Project created.')


@main.command()
def path():
    '''
    Displays the path of the folder of projects.
    '''
    click.echo(
        ProjectFolder(
            ProjectName('None')
        ).get_base_path()
    )


def peek():
    pass


def status():
    '''
    Outputs the status of the current project.
    '''


def switch():
    '''
    Switches to the project with the specified name.
    '''


def undo():
    '''
    Reverts the last command you entered.
    '''
