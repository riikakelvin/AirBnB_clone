#!/usr/bin/python3
'''
Test suite for user
'''
import os
import models
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    '''
    Tests for user
    '''

    def test_name(self):
        '''
        Tests for name inputs
        '''
        pass

if __name__ == '__main__':
    unittest.main()
