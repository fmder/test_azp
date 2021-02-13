import unittest

import azp

class TestAZP(unittest.TestCase):
    def test_azp_true(self):
        self.assertTrue(azp.some_function())