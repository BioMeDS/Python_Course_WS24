import unittest
from functions import ReverseComplement

class TestReverseComplement(unittest.TestCase):

    def test_empty(self):
        self.assertEqual(ReverseComplement(""), "")

    def test_simple(self):
        self.assertEqual(ReverseComplement("ACGTT"), "AACGT")

    def test_caseSensitive(self):
        self.assertEqual(ReverseComplement("AcGt"), "aCgT")
    
    def test_Error(self):
        # check that it fails when the sequence contains illegal characters
        with self.assertRaises(TypeError):
            ReverseComplement(17) # type: ignore
