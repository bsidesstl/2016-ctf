#!/usr/bin/env python
# decrypt.py

import hashlib

def hashdecrypt(msg):
    res = msg.decode('rot13').decode('base64')
    res = [ ord(i) for i in res]
    for i in range(len(res)):
        if i == 12:
            print ''.join([chr(i) for i in res]) # i_lied_no_flag_for_you!
            break

        n = res[-i-2]
        token = hashlib.sha1(chr(n)).digest()
        for c in xrange(32, 127):
            n  = c ^ 0xfe ^ 0xc3 ^ 0x42 ^ 0x21
            n ^= 0xc2 ^ ord(token[0])
            n ^= 0xf3 ^ ord(token[1])
            n ^= 0x27 ^ ord(token[2])
            n ^= 0x4c ^ ord(token[3])
            n ^= 0x21 ^ ord(token[4])
            n ^= 0xfe ^ ord(token[5])
            n ^= 0xa3 ^ ord(token[6])
            n ^= 0xf0 ^ ord(token[7])
            n ^= 0x11 ^ ord(token[6])
            n ^= 0x54 ^ ord(token[5])
            n ^= 0xca ^ ord(token[4])
            n ^= 0x3c ^ ord(token[3])
            n ^= 0x20 ^ ord(token[2])
            n ^= 0xd1 ^ ord(token[1])
            n ^= 0xf2 ^ ord(token[0])
            if n == res[-i-1]:
                res[-i-1] = c    
                break
     
hashdecrypt('vdyXBpHswVlBmzsWct==')
