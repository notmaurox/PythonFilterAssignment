import mathT

def test_calc_total():
    total = mathT.calc_total(4,5)
    assert total == 9
  
def test_calc_multiply():
    result = mathT.calc_multiply(10,3)
    assert result == 30
    