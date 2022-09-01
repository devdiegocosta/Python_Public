#!bin/python
import hashlib
import base64

# rainbow table attack
# Lab ID: 2a90888ad0b436693738646821d351384a596a6d
# hash = md5 --> base64 --> sha1
h1 = '806825f0827b628e81620f0d83922fb2c52c7136'

with open('/usr/share/john/password.lst', 'r') as l:
    for p in l:
        h2 = p.strip('\n')
        h2 = h2.strip('\t')
        h2 = hashlib.md5(h2.encode()).hexdigest()
        h2 = base64.b64encode(h2.encode())
        h2 = hashlib.sha1(h2).hexdigest()

        if (h1 == h2):
            print('broken: ' + p + ' = ' + h2)
