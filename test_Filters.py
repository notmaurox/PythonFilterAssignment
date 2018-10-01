from LIDARFilterClass import LIDARFilter
from rangeFilterClass import rangeFilter
from medianFilterClass import medianFilter
import numpy as np
import pytest

def test_each_filter_has_update():
    
    class badFilter(LIDARFilter):
        def __init__(self,LIDARFilter):
            self.rangeN = LIDARFilter.rangeN
            self.rangeDist = LIDARFilter.rangeDist
            
        def doNothing():
            print "-1"
    
    lFilter = LIDARFilter(200,1000,0.03,50)    
    bFilter = badFilter(lFilter)
    
    with pytest.raises(NotImplementedError):
        bFilter.update( np.array([0.0,0.0,0.0]) )

def test_rangeFilter_update_min():
    lidarFilter = LIDARFilter(0,100,0.03,50)
    rF = rangeFilter( lidarFilter )
    
    expectedOutput = [0.03,0.03,0.03,0.03]
    recievedOutput = rF.update( [-0.02,0.02,-0.02,0.0299999999] )
    
    assert recievedOutput == expectedOutput
    
def test_rangeFilter_update_max():
    lidarFilter = LIDARFilter(0,100,0.03,50)
    rF = rangeFilter( lidarFilter )
    
    expectedOutput = [50.0,50.0,50.0,50.0]
    recievedOutput = rF.update( [51.0,50.5,99.0,50.0] )
    
    assert recievedOutput == expectedOutput
    
def test_rangeFilter_numpyArray_preservation():
    lidarFilter = LIDARFilter(0,100,0.03,50)
    rF = rangeFilter( lidarFilter )
    
    outPut = rF.update( np.array([0.02,1.0,51]) )
    
    assert type(outPut) == np.ndarray
    
def test_medianFilter_median_is_avrg():
    lidarFilter = LIDARFilter(0,100,0.03,50)
    mF = medianFilter( lidarFilter, 2 )
    
    inputArray = [[1,1,1,1],[2,2,2,2]]
    expectedOutput = [[1,1,1,1],[1.5,1.5,1.5,1.5]]
    recievedOutput = []
    
    for inputScan in inputArray:
        recievedOutput.append( mF.update(inputScan) )
        
    assert recievedOutput == expectedOutput
    
def test_medianFilter_median_is_middle():
    lidarFilter = LIDARFilter(0,100,0.03,50)
    mF = medianFilter( lidarFilter, 3 )
    
    inputArray = [[3,3,3,3],[2,2,2,2],[1,1,1,1]]
    expectedOutput = [[3,3,3,3],[2.5,2.5,2.5,2.5],[2,2,2,2]]
    recievedOutput = []
    
    for inputScan in inputArray:
        recievedOutput.append( mF.update(inputScan) )
        
    assert recievedOutput == expectedOutput 

def test_median_example_output():
    providedInput0 = [0.0, 1.0, 2.0, 1.0, 3.0]
    providedInput1 = [1.0, 5.0, 7.0, 1.0, 3.0]
    providedInput2 = [2.0, 3.0, 4.0, 1.0, 0.0]
    providedInput3 = [3.0, 3.0, 3.0, 1.0, 3.0]
    providedInput4 = [10.0, 2.0, 4.0, 0.0, 0.0]
    
    inputList = [providedInput0,providedInput1,providedInput2,providedInput3,providedInput4]
    
    expectedOutput0 = [0.0,1.0,2.0,1.0,3.0]
    expectedOutput1 = [0.5,3.0,4.5,1.0,3.0]
    expectedOutput2 = [1.0,3.0,4.0,1.0,3.0]
    expectedOutput3 = [1.5,3.0,3.5,1.0,3.0]
    expectedOutput4 = [2.5,3.0,4.0,1.0,1.5]
    
    expectedOutputList = [expectedOutput0,expectedOutput1,expectedOutput2,expectedOutput3,expectedOutput4]
    
    lFilter = LIDARFilter(0,100,0.0,99.0)
    mFilter = medianFilter(lFilter,3)
    
    recievedOutputList = []
    for inputArr in inputList:
        recievedOutputList.append( mFilter.update(inputArr) )
    
    print recievedOutputList
    print expectedOutputList
    
    assert recievedOutputList == expectedOutputList

def test_medianFilter_numpyArray_preservation():
    lidarFilter = LIDARFilter(0,100,0.03,50)
    mF = medianFilter( lidarFilter, 2 )
    
    outPut = mF.update( np.array([1,1,2,2]) )
    
    assert type(outPut) == np.ndarray   
        
    