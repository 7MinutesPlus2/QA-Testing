import pytest
from gunsmith_commission import calculate_commission

# Normal Boundary Tests

# Testing on lock boundary
def test_minimum_lock_sales():
    assert calculate_commission(1, 10, 10) > 0

def test_maximum_lock_sales():
    assert calculate_commission(70, 10, 10) > 0

# Testing on stock boundary
def test_minimum_stock_sales():
    assert calculate_commission(10, 1, 10) > 0

def test_maximum_stock_sales():
    assert calculate_commission(10, 80, 10) > 0

# Testing on barrel boundary
def test_minimum_barrel_sales():
    assert calculate_commission(10, 10, 1) > 0

def test_maximum_barrel_sales():
    assert calculate_commission(10, 10, 90) > 0

# Robust Boundary Tests
def test_lock_below_min():
    with pytest.raises(ValueError):
        calculate_commission(0, 10, 10)

def test_lock_above_max():
    with pytest.raises(ValueError):
        calculate_commission(71, 10, 10)

def test_stock_below_min():
    with pytest.raises(ValueError):
        calculate_commission(10, 0, 10)

def test_stock_above_max():
    with pytest.raises(ValueError):
        calculate_commission(10, 81, 10)

def test_barrel_below_min():
    with pytest.raises(ValueError):
        calculate_commission(10, 10, 0)

def test_barrel_above_max():
    with pytest.raises(ValueError):
        calculate_commission(10, 10, 91)

# Worst Case Boundary Tests
def test_worst_case_all_min():
    assert calculate_commission(1, 1, 1) > 0

def test_worst_case_all_max():
    assert calculate_commission(70, 80, 90) > 0
