import numpy as np
from rangeFilterClass import rangeFilter
from medianFilterClass import medianFilter
from LIDARFilterClass import LIDARFilter

#File used for calling methods to make sure they worked as they were built

class garbageFilter(LIDARFilter):
    def doNothing():
        print "doNothing method"

LIDARFilter = LIDARFilter(0,100,0.0,99.0)
rF = rangeFilter( LIDARFilter )
mF = medianFilter( LIDARFilter, 3 )

print type(np.array([0.0,0.0,0.0]))


print rF.update( [0,0,0,0] )
print rF.update( np.array([0.0,0.0,0.0]) )

print mF.update( np.array([0.0, 1.0, 2.0, 1.0, 3.0]) )
print mF.update( np.array([1.0, 5.0, 7.0, 1.0, 3.0]) )
print mF.update( np.array([2.0, 3.0, 4.0, 1.0, 0.0]) )
print mF.update( np.array([3.0, 3.0, 3.0, 1.0, 3.0]) )
print mF.update( np.array([10.0, 2.0, 4.0, 0.0, 0.0]) )


print rF.rangeN
print mF.rangeN
print rF.rangeDist
print mF.rangeDist

