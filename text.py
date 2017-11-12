# -*- coding: latin-1 -*-
# Any of the foloowing string literal forms work in latin-1
# Changing the encoding above to either ascii or utf-8 fails,
# bacause the 0xc4 and 0xe8 in myStr1 are not valid in either.
myStr1 = 'aÄBèC'
myStr2 = 'A\u00c4B\U000000e8C'
mystr3 = 'A' + chr(0xC4) + 'B' + chr(0xE8) + 'C'

import sys

print('Default encoding: ', sys.getdefaultencoding())
for aStr in myStr1, myStr2, mystr3:
    print('{0}, strlent={1}, '.format(aStr, len(aStr)), end='')
    bytes1 = aStr.encode()
    bytes2 = aStr.encode('latin-1')
    # bytes3 = aStr.encode('ascii')
    print('bytelen1={0}, bytelen2={1}'.format(len(bytes1), len(bytes2)))
