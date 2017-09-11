# Set 1
import binascii
import base64
import string
import bitarray
from constants import freqs


# 1) Convert hex to base64
def hexToBase64(hexStr):
    decoded = binascii.unhexlify(hexStr)
    return base64.b64encode(decoded).decode('ascii')

# 2) Fixed XOR
def fixedXOR(hex1, hex2):
    decoded1 = binascii.unhexlify(hex1)
    decoded2 = binascii.unhexlify(hex2)
    XORed = bytes(b1 ^ b2 for (b1, b2) in zip(decoded1, decoded2))
    return binascii.hexlify(XORed).decode('ascii')

# 3) Single-byte XOR cipher
# score function taken from https://crypto.stackexchange.com/questions/30209/developing-algorithm-for-detecting-plain-text-via-frequency-analysis
# Correction, the chi-squared implementation doesn't seem to work
def scoreStr(byteStr):
    # count = [0] * 27
    # total = 0
    # ignored = 0
    # for i in byteStr:
    #     if i >= 65 and i <= 90:
    #         count[i - 65] += 1
    #     elif i >= 97 and i <= 122:
    #         count[i - 97] += 1
    #     elif i == 32:
    #         count[26] += 1
    #     elif i >= 33 and i <= 126:
    #         ignored += 1
    #     elif i == 9 or i == 10 or i == 13:
    #         ignored += 1
    #     else:
    #         return 0
    # length = len(byteStr) - ignored
    # chi2 = 0

    # for i in range(27):
    #     observed = count[i]
    #     letter = chr(i + 97) if i < 26 else ' '
    #     expected = length * freqs[letter]
    #     diff = observed - expected
    #     chi2 += diff * diff / expected
    
    # return chi2
    score = 0
    for i in byteStr:
        c = chr(i).lower()
        if c in freqs:
            score += freqs[c]
    return score

def singleByteXOR(hexStr):
    # iterate all single byte possibilities
    # repeat each byte * the length of the input string
    maxScore = 0
    bestResult = ''
    for n in range(256):
        cipher = hex(n).split('x')[-1] * len(hexStr)
        XORed = fixedXOR(hexStr, cipher)
        score = scoreStr(binascii.unhexlify(XORed))
        if score > maxScore:
            maxScore = score
            bestResult = binascii.unhexlify(XORed)

    return (maxScore, bestResult)
        
# 4) Detecting single byte XORed
def detectSingleByteXOR():
    maxScore = 0
    bestResult = ''
    with open('4.txt', 'r') as inFile:
        for line in inFile:
            # this check should probably be elsewhere
            if len(line) % 2 == 1:
                continue
            score, result = singleByteXOR(line)
            if score > maxScore:
                bestResult = result

# 5) Repeating Key XOR 
def repeatingKeyXOR(plainText, key):
    keyLen = len(key)
    XORed = bytes(b ^ key[i % keyLen] for (i, b) in enumerate(plainText))
    return binascii.hexlify(XORed).decode('ascii')

# 6) Breaking repeating key XOR

# Hamming needs to operate on bits, not strings or bytes
def hammingDistance(str1, str2):
    diff = 0
    bits1 = bitarray.bitarray()
    bits2 = bitarray.bitarray()
    bits1.frombytes(str1)
    bits2.frombytes(str2)

    for i in range(len(bits1)):
        if (bits1[i] != bits2[i]):
            diff += 1
    return diff


def breakRepeatingKeyXOR():
    return False