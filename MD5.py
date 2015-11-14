import math
import struct
import sys
from numbers import Number
from collections import Set, Mapping, deque

try: # Python 2
    zero_depth_bases = (basestring, Number, xrange, bytearray)
    iteritems = 'iteritems'
except NameError: # Python 3
    zero_depth_bases = (str, bytes, Number, range, bytearray)
    iteritems = 'items'

def getsize(obj):
    """Recursively iterate to sum size of object & members."""
    def inner(obj, _seen_ids = set()):
        obj_id = id(obj)
        if obj_id in _seen_ids:
            return 0
        _seen_ids.add(obj_id)
        size = sys.getsizeof(obj)
        if isinstance(obj, zero_depth_bases):
            pass # bypass remaining control flow and return
        elif isinstance(obj, (tuple, list, Set, deque)):
            size += sum(inner(i) for i in obj)
        elif isinstance(obj, Mapping) or hasattr(obj, iteritems):
            size += sum(inner(k) + inner(v) for k, v in getattr(obj, iteritems)())
        # Now assume custom object instances
        elif hasattr(obj, '__slots__'): 
            size += sum(inner(getattr(obj, s)) for s in obj.__slots__ if hasattr(obj, s))
        else: 
            attr = getattr(obj, '__dict__', None)
            if attr is not None:
                size += inner(attr)
        return size
    return inner(obj)


#Rotate Amounts

S = [7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22, 7, 12, 17, 22,
     5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20, 5,  9, 14, 20,
     4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23, 4, 11, 16, 23,
     6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21, 6, 10, 15, 21]

#Byte to Long Converter
def bytes_to_int(bytes):
  return int(bytes.encode('hex'), 16)


#Boolean Functions

def F(X, Y, Z):
    return (X & Y) | (~X & Z)

def G(X, Y, Z):
    return (X & Z) | (Y & ~Z)

def H(X, Y, Z):
    return X ^ Y ^ Z

def I(X, Y, Z):
    return Y ^ (X | ~Z)


#Left Shift

def LeftShift(X, shift):
    #Consider only relevant 32-bits
    X &= 0xFFFFFFFF

    #Left Shift Rotation
    return ((X << shift) | (X>>(32-shift))) & 0xFFFFFFFF


#Initial Values
InitialValues = [0x67452301, 0xefcdab89, 0x98badcfe, 0x10325476]

#T[i] denotes the i-th element of the table, which is equal to the
#integer part of 4294967296 times abs(sin(i)), where i is in radians.
T = [int(abs(math.sin(i+1)) * 2**32) & 0xFFFFFFFF for i in range(64)]

def Function(X, Y, Z, i):
    if(i >= 0 and i < 16):
        return F(X, Y, Z)
    elif (i >= 16 and i < 32):
        return G(X, Y, Z)
    elif (i >= 32 and i <48):
        return H(X, Y, Z)
    elif (i >= 48 and i < 64):
        return I(X, Y, Z)

def IndexFunction(i):
    if(i >= 0 and i < 16):
        return i
    elif (i >= 16 and i < 32):
        return (5*i + 1)%16
    elif (i >= 32 and i < 48):
        return (3*i + 5)%16
    elif (i >= 48 and i < 64):
        return (7*i)%16


def MD5(Message):
    print sys.getsizeof(Message)
    Message = bytearray(Message)
    print sys.getsizeof(Message)
    InitialNumberOfBits = len(Message) * 8
    Message.append(0x80)
    print getsize(Message)
    while((len(Message)*8)%512 != 448):
        Message.append(0)
        print getsize(Message)
    Message.append(0xFFFFFFFF & InitialNumberOfBits)
    print getsize(Message)
    print Message

    HashPieces = InitialValues[:]
    
    for w in range(0, len(Message), 64):
        A, B, C, D = HashPieces
        Chunk = Message[w:w+64]
        print HashPieces
        for i in range(64):
            F = Function(i, B, C, D)
            print F
            g = IndexFunction(i)
            dTemp = D
            D = C
            
            print Chunk[4*g:4*g+4]
            temp = A + F + T[i] + bytes_to_int(Chunk[4*g: 4*g+4])
            B = B + LeftShift(temp, S[i])
            A = dTemp
            
        
        HashPieces[0] += A 
        HashPieces[0] &= 0xFFFFFFFF
        HashPieces[1] += B 
        HashPieces[1] &= 0xFFFFFFFF
        HashPieces[2] += C 
        HashPieces[2] &= 0xFFFFFFFF
        HashPieces[3] += D 
        HashPieces[3] &= 0xFFFFFFFF

    return sum(x<<(32*i) for i, x in enumerate(HashPieces))

##def MD5toHex(Digest):
##    raw = Digest.to_bytes(16, byteorder='little')
##    return '{:032x}'.format(int.from_bytes(raw, byteorder='big'))

        
if __name__ == "__main__":
    message = "abc"
    print MD5(message)
