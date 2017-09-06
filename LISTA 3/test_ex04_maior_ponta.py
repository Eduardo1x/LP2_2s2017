from ex04 import maior_ponta
  

def test_ex04():
  print ('Maior_ponta')
  assert maior_ponta([1, 2, 3]) == [3, 3, 3]
  assert maior_ponta([11, 5, 9]) == [11, 11, 11]
  assert maior_ponta([2, 11, 3]) == [3, 3, 3]
  assert maior_ponta([11, 3, 3]) == [11, 11, 11]
  assert maior_ponta([3, 11, 11]) == [11, 11, 11]
  assert maior_ponta([2, 2, 2]) == [2, 2, 2]
  assert maior_ponta([2, 11, 2]) == [2, 2, 2]
  assert maior_ponta([0, 0, 1]) == [1, 1, 1]


