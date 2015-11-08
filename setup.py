'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
from setuptools import setup, find_packages

setup(
    name='ShellFash',
    version='0.0.1',
    description='TODO',  # TODO: Finish
    long_description='TODO',  # TODO: Finish
    url='https://github.com/tyost/ShellFash',
    author='Tim Yost',
    license='MIT',
    classifiers=[
        'Topic :: Desktop Environment',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4'
    ],
    keywords='', # TODO: Keywords
    packages=find_packages(exclude=['test*']),
    install_requires=[
        'appdirs>=1.4',
        'click>=5,<6',
        'pyfakefs',
        'wxPython_Phoenix>=3'
    ],
    entry_points = '''
        [console_scripts]
        shelf=shellfash.view.console:main
    '''
)
