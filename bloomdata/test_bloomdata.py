import bloomdata.bloomdata as bd
import pytest

def test_increment_int():
    assert bd.increment(3) == 4
    assert bd.increment(-2) == -1

def test_increment_float():
    assert bd.increment(3.5) == 4.5

def test_increment_return_type():
    assert isinstance(bd.increment(3) , int)