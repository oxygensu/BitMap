import ctypes

c_uint32 = ctypes.c_uint32

class A429_label(ctypes.LittleEndianStructure):
    _fields_ = [
        ("bit1", c_uint32, 1),
        ("bit2", c_uint32, 1),
        ("bit3", c_uint32, 1),
        ("bit4", c_uint32, 1),
        ("bit5", c_uint32, 1),
        ("bit6", c_uint32, 1),
        ("bit7", c_uint32, 1),
        ("bit8", c_uint32, 1),
        ("bit9", c_uint32, 1),
        ("bit10", c_uint32, 1),
        ("bit11", c_uint32, 1),
        ("bit12", c_uint32, 1),
        ("bit13", c_uint32, 1),
        ("bit14", c_uint32, 1),
        ("bit15", c_uint32, 1),
        ("bit16", c_uint32, 1),
        ("bit17", c_uint32, 1),
        ("bit18", c_uint32, 1),
        ("bit19", c_uint32, 1),
        ("bit20", c_uint32, 1),
        ("bit21", c_uint32, 1),
        ("bit22", c_uint32, 1),
        ("bit23", c_uint32, 1),
        ("bit24", c_uint32, 1),
        ("bit25", c_uint32, 1),
        ("bit26", c_uint32, 1),
        ("bit27", c_uint32, 1),
        ("bit28", c_uint32, 1),
        ("bit29", c_uint32, 1),
        ("bit30", c_uint32, 1),
        ("bit31", c_uint32, 1),
        ("bit32", c_uint32, 1),
    ]

class Union(ctypes.Union):
    _fields_ = [
        ("label", A429_label),
        ("asbyte", c_uint32)
    ]
