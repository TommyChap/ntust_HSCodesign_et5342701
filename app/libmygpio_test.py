from ctypes import *
lib = CDLL("./libmygpio.so")
lib.init()
# Read Switch value
data = lib.Read(0)
lib.Write(r, 0)
print(data)
# Read Button value
data = lib.Read(1)
lib.Write(r, 0)
print(data)
