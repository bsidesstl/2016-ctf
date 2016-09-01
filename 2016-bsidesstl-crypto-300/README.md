
Dr. Meade has developed a proprietary unbreakable encryption
algorithm. Your job is to break his encryption. You flag is
in the plaintext.

```
def hashcrypt(msg, key):
    token = hashlib.sha1(key).digest()
    res = ""
    for c in msg:
        n = ord(c) ^ 0xfe ^ 0xc3 ^ 0x42 ^ 0x21
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
        res += chr(n)
        token = hashlib.sha1(chr(n)).digest()
    return res.encode('base64').encode('rot13')
```

Ciphertext: vdyXBpHswVlBmzsWct==

Hint: The start and the beginning is reached by following the same path.

Flag: STL-83df8a11
