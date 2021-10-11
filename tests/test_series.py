from math_series.series import fibonacci

def test_firstTest():
    l=0
    assert fibonacci(l)=="Incorrect input"
def test_firstTest1():
    l=-5
    assert fibonacci(l)=="Incorrect input"
def test_firstTest3():
    l=1
    assert fibonacci(l)==0