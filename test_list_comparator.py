import pytest
from list_comparator import ListComparator

def test_average_empty_list():
    """Test average calculation for an empty list."""
    comparator = ListComparator([], [])
    assert comparator.average([]) == 0

def test_average_normal_list():
    """Test average calculation for a normal list."""
    comparator = ListComparator([1, 2, 3], [4, 5, 6])
    assert comparator.average([1, 2, 3]) == 2

def test_compare_averages_first_greater():
    """Test comparison when the first list has a greater average."""
    comparator = ListComparator([10, 20, 30], [1, 2, 3])
    assert comparator.compare_averages() == "Первый список имеет большее среднее значение"

def test_compare_averages_second_greater():
    """Test comparison when the second list has a greater average."""
    comparator = ListComparator([1, 2, 3], [10, 20, 30])
    assert comparator.compare_averages() == "Второй список имеет большее среднее значение"

def test_compare_averages_equal():
    """Test comparison when both lists have equal averages."""
    comparator = ListComparator([4, 5, 6], [4, 5, 6])
    assert comparator.compare_averages() == "Средние значения равны"
