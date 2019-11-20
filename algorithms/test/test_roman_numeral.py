
# 
# Your previous Plain Text content is preserved below:
# 
# This is just a simple shared plaintext pad, with no execution capabilities.
# 
# When you know what language you'd like to use for your interview,
# simply choose it from the dropdown in the top bar.
# 
# You can also change the default language your pads are created with
# in your account settings: https://coderpad.io/settings
# 
# Enjoy your interview!
# 

# Symbol  I  V  X  L    C    D    M
# Value  1  5  10  50  100  500  1,000


numerals = {
  1: 'I',
  # 4: 'IV',
  5: 'V',
  # 9: 'IX',
  10: 'X',
  # 40: 'XL',
  50: 'L',
  # 90: 'XC',
  100: 'C',
  # 400: 'CD',
  500: 'D',
  # 900: 'CM',
  1000: 'M'
}


import unittest


def get_roman_numeral(arabic_numeral):
    #Recorrer numerals
    roman_numeral = ''
    numerals_arr = numerals.keys()
    #numerals_arr = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    numerals_arr = sorted(numerals_arr, reverse = True)
    # enumerate(list_a) -> el, idx
    
    for i in numerals_arr: # 1000, 900, ...
        if arabic_numeral - i < 0:
            continue
        while arabic_numeral - i >= 0 : 
            arabic_numeral -= i
            roman_numeral += numerals[i] 
        
        if arabic_numeral == 0:
            return roman_numeral
          
    ###################################################
    roman_numeral = ''
    numerals_arr = numerals.keys()
    numerals_arr = sorted(numerals_arr, reverse = True)
    
    while arabic_numeral > 0:
      for n in numerals_arr:
        if arabic_numeral - n >= 0: # We can substract this
          arabic_numeral = arabic_numeral - n
          roman_numeral += numerals[n]
          break
          
    return roman_numeral
    ###################################################


class TestRomanNumeral(unittest.TestCase):
  
  def test_roman_numeral(self):
    tests = [
      (1, 'I'),
      (4, 'IV'),
      (14, 'XIV'),
      (16, 'XVI'), # 10 + 5 + 1 -> 16 - 10 - 5 - 1 = 0
      (255, 'CCLV'),
      (490, 'CDXC'),
      (1094, 'MXCIV'),
    ]
    for test in tests:
      self.assertEqual(get_roman_numeral(test[0]), test[1])

      
unittest.main()