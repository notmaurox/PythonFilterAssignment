import numpy as np
from rangeFilter import rangeFilter
from medianFilter import medianFilter
from FilterClass import LIDARFilter

class garbageFilter(LIDARFilter):
    def doNothing():
        print "yeet"

rF = rangeFilter()

gF = garbageFilter()

mF = medianFilter(3)
print mF.update( np.array([0.0, 1.0, 2.0, 1.0, 3.0]) )
print mF.update( np.array([1.0, 5.0, 7.0, 1.0, 3.0]) )
print mF.update( np.array([2.0, 3.0, 4.0, 1.0, 0.0]) )
print mF.update( np.array([3.0, 3.0, 3.0, 1.0, 3.0]) )
print mF.update( np.array([10.0, 2.0, 4.0, 0.0, 0.0]) )


print rF.rangeN
print mF.rangeN
print rF.rangeDist
print mF.rangeDist

# gF.update( np.array([1.0, 2.0, 3.0]) ) <- throws NotImplementedError
