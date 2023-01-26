#Imports necesarios para que wr_bmp y otras clases funcionen
#implentacion vista en graficas

import struct

def char(c):
    return struct.pack('=c', c.encode('ascii'))

def word(w):
    return struct.pack('=h', w)

def dword(d):
    return struct.pack('=l', d)

def color(r,g,b):
    return bytes([b, g, r])
