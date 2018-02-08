NAME = "enlist"

CODEPAGE = {
    0: '¡', 1: '¢', 2: '£', 3: '¤', 4: '¥', 5: '¦', 6: '©', 7: '¬',
    8: '®', 9: 'µ', 10: 'π', 11: '¿', 12: '€', 13: 'Æ', 14: 'Ç', 15: 'Ð',
    16: 'Ñ', 17: '×', 18: 'Ø', 19: 'Œ', 20: 'Þ', 21: 'ß', 22: 'æ', 23: 'ç',
    24: 'ð', 25: 'ı', 26: 'ȷ', 27: 'ñ', 28: '÷', 29: 'ø', 30: 'œ', 31: 'þ',
    32: ' ', 33: '!', 34: '"', 35: '#', 36: '$', 37: '%', 38: '&', 39: "'",
    40: '(', 41: ')', 42: '*', 43: '+', 44: ',', 45: '-', 46: '.', 47: '/',
    48: '0', 49: '1', 50: '2', 51: '3', 52: '4', 53: '5', 54: '6', 55: '7',
    56: '8', 57: '9', 58: ':', 59: ';', 60: '<', 61: '=', 62: '>', 63: '?',
    64: '@', 65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G',
    72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M', 78: 'N', 79: 'O',
    80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W',
    88: 'X', 89: 'Y', 90: 'Z', 91: '[', 92: '\\', 93: ']', 94: '^', 95: '_',
    96: '`', 97: 'a', 98: 'b', 99: 'c', 100: 'd', 101: 'e', 102: 'f', 103: 'g',
    104: 'h', 105: 'i', 106: 'j', 107: 'k', 108: 'l', 109: 'm', 110: 'n', 111: 'o',
    112: 'p', 113: 'q', 114: 'r', 115: 's', 116: 't', 117: 'u', 118: 'v', 119: 'w',
    120: 'x', 121: 'y', 122: 'z', 123: '{', 124: '|', 125: '}', 126: '~', 127: '¶',
    128: '°', 129: '¹', 130: '²', 131: '³', 132: '⁴', 133: '⁵', 134: '⁶', 135: '⁷',
    136: '⁸', 137: '⁹', 138: '⁺', 139: '⁻', 140: '⁼', 141: '⁽', 142: '⁾', 143: '±',
    144: '≤', 145: '≠', 146: '≥', 147: '√', 148: '·', 149: '∆', 150: '₱', 151: '•',
    152: '†', 153: '‡', 154: '§', 155: '⍺', 156: '⍵', 157: 'ŝ', 158: 'σ', 159: '←',
    160: '↑', 161: '→', 162: '↓', 163: '↔', 164: '↕', 165: '↙', 166: '↘', 167: '↶',
    168: '↷', 169: '↻', 170: 'λ', 171: 'Ạ', 172: 'Ḅ', 173: 'Ḍ', 174: 'Ẹ', 175: 'Ḥ',
    176: 'Ị', 177: 'Ḳ', 178: 'Ḷ', 179: 'Ṃ', 180: 'Ṇ', 181: 'Ọ', 182: 'Ṛ', 183: 'Ṣ',
    184: 'Ṭ', 185: 'Ụ', 186: 'Ṿ', 187: 'Ẉ', 188: 'Ỵ', 189: 'Ẓ', 190: 'Ȧ', 191: 'Ḃ',
    192: 'Ċ', 193: 'Ḋ', 194: 'Ė', 195: 'Ḟ', 196: 'Ġ', 197: 'Ḣ', 198: 'İ', 199: 'Ŀ',
    200: 'Ṁ', 201: 'Ṅ', 202: 'Ȯ', 203: 'Ṗ', 204: 'Ṙ', 205: 'Ṡ', 206: 'Ṫ', 207: 'Ẇ',
    208: 'Ẋ', 209: 'Ẏ', 210: 'Ż', 211: 'ạ', 212: 'ḅ', 213: 'ḍ', 214: 'ẹ', 215: 'ḥ',
    216: 'ị', 217: 'ḳ', 218: 'ḷ', 219: 'ṃ', 220: 'ṇ', 221: 'ọ', 222: 'ṛ', 223: 'ṣ',
    224: 'ṭ', 225: 'ụ', 226: 'ṿ', 227: 'ẉ', 228: 'ỵ', 229: 'ẓ', 230: 'ȧ', 231: 'ḃ',
    232: 'ċ', 233: 'ḋ', 234: 'ė', 235: 'ḟ', 236: 'ġ', 237: 'ḣ', 238: 'ŀ', 239: 'ṁ',
    240: 'ṅ', 241: 'ȯ', 242: 'ṗ', 243: 'ṙ', 244: 'ṡ', 245: 'ṫ', 246: 'ẇ', 247: 'ẋ',
    248: 'ẏ', 249: 'ż', 250: '«', 251: '»', 252: '‘', 253: '’', 254: '“', 255: '”'
}
