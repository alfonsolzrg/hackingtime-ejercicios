import unittest

def get_roman_numeral(arabic_numeral):
  roman_numeral = 'I'
  return roman_numeral

def TestRomanNumeral(unittest.TestCase):
  tests = [
    (1, 'I'),
    (4, 'IV'),
    (14, 'XIV'),
    (255, 'CCLV'),
    (490, 'CDXC'),
    (1094, 'MXCIV'),
  ]
  for test in tests:
    self.assertEqual(get_roman_numeral(test[0]), test[1])