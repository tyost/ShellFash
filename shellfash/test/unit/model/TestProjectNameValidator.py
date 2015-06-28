# -*- coding: utf-8 -*-
'''
License:
    Copyright (c) 2015 Tim Yost
    This code is licensed to you under an open source license (MIT/X11).
    See the LICENSE file for details.
'''
import unittest
from shellfash.model.ProjectNameValidator import ProjectNameValidator


class TestProjectNameValidator(unittest.TestCase):
    '''
    Tests for ProjectNameValidator.
    '''

    def setUp(self):
        self.validator = ProjectNameValidator()

    
    def test_ProjectName_AllowStart(self):
        self.assertTrue(self.validator.validate('1z'))
        self.assertTrue(self.validator.validate('az'))
        self.assertTrue(self.validator.validate('Az'))
        self.assertTrue(self.validator.validate('_z'))
    
    def test_ProjectName_AllowMiddle(self):
        self.assertTrue(self.validator.validate('z1z'))
        self.assertTrue(self.validator.validate('zaz'))
        self.assertTrue(self.validator.validate('zAz'))
        self.assertTrue(self.validator.validate('z_z'))
        self.assertTrue(self.validator.validate('z z'))
        self.assertTrue(self.validator.validate('z.z'))
        self.assertTrue(self.validator.validate('z-z'))
    
    def test_ProjectName_AllowEnd(self):
        self.assertTrue(self.validator.validate('z1'))
        self.assertTrue(self.validator.validate('za'))
        self.assertTrue(self.validator.validate('zA'))
        self.assertTrue(self.validator.validate('z_'))
    
    def test_ProjectName_DisallowEmpty(self):
        self.assertFalse(self.validator.validate(''))
        self.assertFalse(self.validator.validate(' '))
    
    def test_ProjectName_DisallowStart(self):
        self.assertFalse(self.validator.validate(' z'))
        self.assertFalse(self.validator.validate('-z'))
        self.assertFalse(self.validator.validate('.z'))
    
    def test_ProjectName_NoTrailingSpecialSymbols(self):
        self.assertFalse(self.validator.validate('z '))
        self.assertFalse(self.validator.validate('z-'))
        self.assertFalse(self.validator.validate('z.'))
    
    def test_ProjectName_DisallowOtherSymbols(self):
        self.assertFalse(self.validator.validate('!'))
        self.assertFalse(self.validator.validate('/'))
        self.assertFalse(self.validator.validate('\\'))
        self.assertFalse(self.validator.validate('Փ'))
        self.assertFalse(self.validator.validate('a/a'))
    

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
