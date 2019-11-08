# Sorting exercises
from functools import wraps
import gc
import timeit

import random
import unittest


def timing(f):
  @wraps(f)
  def wrapper(*args, **kwargs):
    gc.disable()
    start_time = timeit.default_timer()
    try:
      result = f(*args, **kwargs)
    finally:
      elapsed = timeit.default_timer() - start_time
      gc.enable()
      print("Time elapsed: {}".format(elapsed))
    return result
  return wrapper


def exch(arr, a, b):
  tmp = arr[a]
  arr[a] = arr[b]
  arr[b] = tmp

@timing
def selection_sort(arr):
  """
  idx = [0, 1, 2, 3, 4]
  arr = [5, 7, 8, 1, 4]
  
  for index in arr:
    go through array and find min
    exch min with elem at position indicated by index
  
  For example, 
    idx = 0: min -> 1 at pos 3 -> exch arr, 0, 3 --- arr = [1, 7, 8, 5, 4]
    idx = 1: min -> 4 at pos 4 -> exch arr, 1, 4 --- arr = [1, 4, 8, 5, 7]
    idx = 2: min -> 5 at pos 3 -> exch arr, 2, 3 --- arr = [1, 4, 5, 8, 7]
    idx = 3: min -> 7 at pos 4 -> exch arr, 3, 4 --- arr = [1, 4, 5, 7, 8]

  - Running time is insensitive to input: it takes about as long to run 
    selection sort for an array that is already in order or for an array with 
    all keys equal as it does for a randomly-ordered array!
  - Data movement is minimal: we only move one element at a time

  Algorithm classification criteria:
  - In-place, or not in-place? In-place.
  - Stable? Yes, it takes the same time no matter the shape of the input
  - Complexity?
    - Memory: O(N) -> lineal
    - Processing: O(N^2) -> N*(N-1) -> N^2 + N
  """
  N = len(arr)
  for i in range(N): # If N = 3, range(N) -> [0, 1, 2]
    min = i
    for j in range(i, N):
      if arr[j] < arr[min]:
        min = j
    exch(arr, i, min)
  return arr

@timing
def insertion_sort(arr):
  """
  idx = [0, 1, 2, 3, 4]
  arr = [5, 7, 8, 1, 4]
  
  for forward_index in arr:
    for backwards_index from forward_index, with a step of -1 until it gets to 0:
      of the two elements in backward_index, backwards_index - 1, compare:
        if backwards_index - 1 is bigger, exch elem for elem in backwards_index.
  
  For example, 
    fwd = 1; bwd = 1 -> compare 5 in pos 0 (bwd-1) vs 7 in pos 1 (bwd). 
      7 is bigger, so it stays --- arr = [5, 7, 8, 1, 4]
    
    fwd = 2; bwd = 2 -> compare 7 in pos 1 (bwd-1) vs 8 in pos 2 (bwd). 
      8 is bigger, so it stays --- arr = [5, 7, 8, 1, 4]
    fwd = 2; bwd = 1 -> compare 5 in pos 0 (bwd-1) vs 7 in pos 1 (bwd). 
      7 is bigger, so it stays --- arr = [5, 7, 8, 1, 4]
    
    fwd = 3; bwd = 3 -> compare 8 in pos 2 (bwd-1) vs 1 in pos 3 (bwd). 
      8 is bigger, so move 1 to the left one position --- arr = [5, 7, 1, 8, 4]
    fwd = 3; bwd = 2 -> compare 7 in pos 1 (bwd-1) vs 1 in pos 2 (bwd). 
      7 is bigger, so move 1 to the left one position --- arr = [5, 1, 7, 8, 4]
    fwd = 3; bwd = 1 -> compare 5 in pos 0 (bwd-1) vs 1 in pos 1 (bwd). 
      5 is bigger, so move 1 to the left one position --- arr = [1, 5, 7, 8, 4]

    fwd = 4; bwd = 4 -> compare 8 in pos 3 (bwd-1) vs 4 in pos 4 (bwd). 
      8 is bigger, so move 4 to the left one position --- arr = [1, 5, 7, 4, 8]
    fwd = 4; bwd = 3 -> compare 7 in pos 2 (bwd-1) vs 4 in pos 3 (bwd). 
      7 is bigger, so move 4 to the left one position --- arr = [1, 5, 4, 7, 8]
    fwd = 4; bwd = 2 -> compare 5 in pos 1 (bwd-1) vs 4 in pos 2 (bwd). 
      5 is bigger, so move 4 to the left one position --- arr = [1, 4, 5, 7, 8]
    fwd = 4; bwd = 1 -> compare 1 in pos 0 (bwd-1) vs 4 in pos 1 (bwd). 
      4 is bigger, so it stays --- arr = [1, 4, 5, 7, 8]
    
  Insertion sort is an excellent method for partially sorted arrays and is 
  also a fine method for tiny arrays.

  Algorithm classification criteria:
    - In-place, or not in-place? In-place.
    - Stable? No. Best case: already sorted, O(N). Worst case, sorted backwards: O(N^2)
    - Complexity?
      - Memory: O(N) -> lineal
      - Processing: O(N) - O(N^2)
  """
  for i in range(1, len(arr)):
    for j in range(i, 0, -1): # range(start=0, stop, step=1) range(2, 10, 2) -> [2, 4, 6, 8]
      if arr[j-1] > arr[j]:
        exch(arr, j, j-1)
  return arr

  # fwd_idx = 0
  # while fwd_idx < len(arr):
  #   bwd_idx = fwd_idx
  #   while fwd_idx >= 0:
  #     if arr[fwd_idx] > arr[bwd_]


@timing
def shell_sort(arr):
  """
  from book.page(271) import explanation
  See book page 271 for explanations on how this works

  Shell sort is an excellent method for partially sorted arrays and is 
  also a fine method for tiny arrays.
  It's hard to find an array for which this algorithm would run slow.

  Algorithm classification criteria:
    - In-place, or not in-place? In-place.
    - Stable? No. Best case: already sorted, O(N). Worst case, sorted backwards: O(N^3/2)
    - Complexity?
      - Memory: O(N) -> lineal
      - Processing: O(N) - O(N^3/2)
  """
  # First, get to the largest possible h number
  h = 1
  N = len(arr)
  while h < N/3:
    h = 3 * h + 1 # h is going to be as big as possible
  # Then, do insertion sort, but by h-grouped subsets
  while h >= 1:
    i = h 
    while i < N:
      j = i
      while j >= h:
        if arr[j-h] > arr[j]:
          exch(arr, j, j-h)
        j -= h
      i += 1
    h = h/3
  return arr

@timing
def merge_sort(arr):
  """
  from book.page(285) import explanation

  arr = [5, 7, 8, 1, 4]
  
  It's an example of a divide and conquer algorithm, it's fast, but 
  it requires an extra array for the merge.

  Algorithm classification criteria:
    - In-place, or not in-place? In-place.
    - Stable? No. Best case: already sorted, O(N). Worst case, sorted backwards: O(N^3/2)
    - Complexity?
      - Memory: O(N) -> lineal
      - Processing: O(N) - O(N^3/2)
  """
  aux = []
  sort(arr, 0, len(arr) - 1)

  def sort(arr, left, right):
    if right - left <= 0:
      return
    middle = (left - right) / 2 # This is the place where the array gets split
    sort(arr, left, mid)
    sort(arr, mid + 1, right)
    merge(arr, left, mid, right)

  def merge(arr, left, middle, right):
    i = left
    j = middle + 1

    for k in range(left, right + 1):
      aux[k] = a[k]

    for k in range(left, right + 1):
      if i > middle: 
        a[k] = aux[j]
        j += 1
      elif j > right: 
        a[k] = aux[i]
        i += 1
      elif aux[j] < aux[i]:
        a[k] = aux[j]
        j += 1
      else:
        a[k] = aux[i]
        i += 1

@timing
def quick_sort(arr):
  pass

def heap_sort(arr):
  pass
