from LIDARFilterClass import LIDARFilter
from rangeFilterClass import rangeFilter
from medianFilterClass import medianFilter
import numpy as np
import pytest

@pytest.fixture
def smallRangeFilter():
    lidarFilter = LIDARFilter(1,100,0.03,50)
    rF = rangeFilter( lidarFilter )
    return rF
    
@pytest.fixture
def smallMedianFilter():
    lidarFilter = LIDARFilter(1,100,0.00,50)
    mF = medianFilter( lidarFilter, 3 )
    return mF
    
def test_each_filter_has_update():
    
    class badFilter(LIDARFilter):
        def __init__(self,LIDARFilter):
            self.rangeN = LIDARFilter.rangeN
            self.rangeDist = LIDARFilter.rangeDist
            
        def doNothing():
            print "-1"
    
    lFilter = LIDARFilter(0,1000,0.03,50)    
    bFilter = badFilter(lFilter)
    
    with pytest.raises(NotImplementedError):
        bFilter.update( np.array([0.0,0.0,0.0]) )

def test_rangeFilter_update_min(smallRangeFilter):
    expectedOutput = [0.03,0.03,0.03,0.03]
    receivedOutput = smallRangeFilter.update( [-0.02,0.02,-0.02,0.0299999999] )
    assert receivedOutput == expectedOutput
    
def test_rangeFilter_update_max(smallRangeFilter):
    expectedOutput = [50.0,50.0,50.0,50.0]
    receivedOutput = smallRangeFilter.update( [51.0,50.5,99.0,50.0] )
    
    assert receivedOutput == expectedOutput
    
def test_rangeFilter_longArray(smallRangeFilter):
    badArray = [0]*101
    expectedOutput = -1 #error code for bad input
    receivedOutput = smallRangeFilter.update(badArray)
    
    assert expectedOutput == receivedOutput
    
def test_rangeFilter_shortArray(smallRangeFilter):
    badArray = []
    expectedOutput = -1 #error code for bad input
    receivedOutput = smallRangeFilter.update(badArray)
    
    assert expectedOutput == receivedOutput
    
def test_rangeFilter_numpyArray_preservation(smallRangeFilter):
    outPut = smallRangeFilter.update( np.array([0.02,1.0,51]) )
    assert type(outPut) == np.ndarray

def test_medianFilter_shortArray(smallMedianFilter):
    badArray = []
    expectedOutput = -1 #error code for bad input
    receivedOutput = smallMedianFilter.update(badArray)
    
    assert expectedOutput == receivedOutput
    
def test_medianFilter_longArray(smallMedianFilter):
    badArray = [0]*101
    expectedOutput = -1 #error code for bad input
    receivedOutput = smallMedianFilter.update(badArray)
    
    assert expectedOutput == receivedOutput
    
def test_medianFilter_inconsistent_arraySize(smallMedianFilter):
    smallMedianFilter.update([1,1,1,1])
    badArray = [0]*20
    expectedOutput = -1 #error code for bad input
    receivedOutput = smallMedianFilter.update(badArray)
    
    assert expectedOutput == receivedOutput

def test_medianFilter_median_is_input(smallMedianFilter):
    inputArray = [1,1,1,2]
    expectedOutput = [1,1,1,2]
    receivedOutput = smallMedianFilter.update(inputArray)
    
    assert expectedOutput == receivedOutput

def test_medianFilter_median_is_avrg(smallMedianFilter):
    inputArray = [[1,1,1,1],[2,2,2,2]]
    expectedOutput = [[1,1,1,1],[1.5,1.5,1.5,1.5]]
    receivedOutput = []
    
    for inputScan in inputArray:
        receivedOutput.append( smallMedianFilter.update(inputScan) )
        
    assert receivedOutput == expectedOutput
    
def test_medianFilter_median_is_middle(smallMedianFilter):
    inputArray = [[3,3,3,3],[2,2,2,2],[1,1,1,1]]
    expectedOutput = [[3,3,3,3],[2.5,2.5,2.5,2.5],[2,2,2,2]]
    receivedOutput = []
    
    for inputScan in inputArray:
        receivedOutput.append( smallMedianFilter.update(inputScan) )
        
    assert receivedOutput == expectedOutput 

def test_medianFilter_provided_example_output(smallMedianFilter):
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
    
    receivedOutputList = []
    for inputArr in inputList:
        receivedOutputList.append( smallMedianFilter.update(inputArr) )
    
    print receivedOutputList
    print expectedOutputList
    
    assert receivedOutputList == expectedOutputList

def test_medianFilter_numpyArray_preservation(smallMedianFilter):    
    outPut = smallMedianFilter.update( np.array([1,1,2,2]) )
    assert type(outPut) == np.ndarray   
        
    