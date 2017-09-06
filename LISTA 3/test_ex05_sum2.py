from ex05 import sum2


def test_ex05():
  print ('sum2')
  assert sum2([1, 2, 3]) == 3
  assert sum2([1, 1]) == 2
  assert sum2([1, 1, 1, 1]) == 2
  assert sum2([1, 2]) == 3
  assert sum2([1]) == 1
  assert sum2([]) == 0
  assert sum2([4, 5, 6]) == 9
  assert sum2([4]) == 4

