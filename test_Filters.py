from LIDARFilterClass import LIDARFilter
from rangeFilterClass import rangeFilter
from medianFilterClass import medianFilter
import numpy as np

def test_median_example_output():
    providedInput0 = np.array([0.0, 1.0, 2.0, 1.0, 3.0]) 
    providedInput1 = np.array([1.0, 5.0, 7.0, 1.0, 3.0])
    providedInput2 = np.array([2.0, 3.0, 4.0, 1.0, 0.0])
    providedInput3 = np.array([3.0, 3.0, 3.0, 1.0, 3.0])
    providedInput4 = np.array([10.0, 2.0, 4.0, 0.0, 0.0])
    
    inputList = [providedInput0,providedInput1,providedInput2,providedInput3,providedInput4]
    
    expectedOutput0 = np.array([0.0,1.0,2.0,1.0,3.0])
    expectedOutput1 = np.array([0.5,3.0,4.5,1.0,3.0])
    expectedOutput2 = np.array([1.0,3.0,4.0,1.0,3.0])
    expectedOutput3 = np.array([1.5,3.0,3.5,1.0,3.0])
    expectedOutput4 = np.array([2.5,3.0,4.0,1.0,1.5])
    
    expectedOutputList = [expectedOutput0,expectedOutput1,expectedOutput2,expectedOutput3,expectedOutput4]
    
    lFilter = LIDARFilter(0,100,0.0,99.0)
    mFilter = medianFilter(lFilter,3)
    
    recievedOutputList = []
    for inputArr in inputList:
        recievedOutputList.append( mFilter.update(inputArr) )
    
    areIdentical = np.array_equal(recievedOutputList, expectedOutputList)
    
    if areIdentical == False:
        print "recieved median filter output"
        print recievedOutputList
        print "expected median filter output"
        print expectedOutputList
    
    assert areIdentical == True
        
    