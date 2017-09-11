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

        # need to figure out how to test this
        self.assertEqual(True, True)

    def test_detectSingleByteXOR(self):
        actual = set1.detectSingleByteXOR()
        
         # need to figure out how to test this
        self.assertEqual(True, True)

    def test_repeatingKeyXOR(self):
        test = b'''Burning 'em, if you ain't quick and nimble
I go crazy when I hear a cymbal'''

        expected = '0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f'

        actual = set1.repeatingKeyXOR(test, b'ICE')
        self.assertEqual(actual, expected)

    def test_hammingDistance(self):
        str1 = b'this is a test'
        str2 = b'wokka wokka!!!'
        expected = 37
        actual = set1.hammingDistance(str1, str2)
        print('HAMMING', actual)

if __name__ == '__main__':
    unittest.main()