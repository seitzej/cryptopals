import unittest

import set1

class TestSet1(unittest.TestCase):
    def test_hexToBase64(self):
        hexStr = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        expected = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        actual = set1.hexToBase64(hexStr)
        
        self.assertEqual(actual, expected)


    def test_fixedXOR(self):
        str1 = '1c0111001f010100061a024b53535009181c'
        str2 = '686974207468652062756c6c277320657965'
        expected = '746865206b696420646f6e277420706c6179'
        actual = set1.fixedXOR(str1, str2)

        self.assertEqual(actual, expected)

    def test_singleByteXOR(self):
        hexStr = '1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'
        actual = set1.singleByteXOR(hexStr)

        self.assertEqual(True, False)
if __name__ == '__main__':
    unittest.main()