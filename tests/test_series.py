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
def test_firstTest4():
    l=2
    assert fibonacci(l)==1
def test_firstTest5():
    l=3
    assert fibonacci(l)==1
def test_firstTest6():
    l=4
    assert fibonacci(l)==2
def test_firstTest7():
    l=5
    assert fibonacci(l)==3
def test_firstTest8():
    l=10
    assert fibonacci(l)==34