from math_series.series import fibonacci
from math_series.series import lucas
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
    ###################################
################  Lucas ##############
##################################

def test_lucas():
    input=0
    assert lucas(input)==2
def test_lucas1():
    input=1
    assert lucas(input)==1
def test_lucas2():
    input=9
    assert lucas(input)==76
def test_lucas3():
    input=4
    assert lucas(input)==7
def test_lucas4():
    input=7
    assert lucas(input)==29

