# Sorting exercises
import random
import unittest

from sorting_algorithms import selection_sort, insertion_sort, shell_sort


class SortingTests(unittest.TestCase):
  def setUp(self):
    self.arr = [random.randrange(0, 100) for _ in range(10000)]

  def test_selection_sort(self):
    print('Selection sort')
    result = selection_sort(self.arr)
    self.assertEquals(result, sorted(self.arr))

  def test_insertion_sort(self):
    print('Insertion sort random scenario')
    result = insertion_sort(self.arr)

    print('Insertion sort worst case scenario')
    result = insertion_sort(sorted(self.arr, reverse=True))

    print('Insertion sort best case scenario')
    result = insertion_sort(sorted(self.arr))
    self.assertEquals(result, sorted(self.arr))

  def test_shell_sort(self):
    print('shell sort random scenario')
    result = shell_sort(self.arr)

    print('shell sort worst case scenario')
    result = shell_sort(sorted(self.arr, reverse=True))

    print('shell sort best case scenario')
    result = shell_sort(sorted(self.arr))
    self.assertEquals(result, sorted(self.arr))
