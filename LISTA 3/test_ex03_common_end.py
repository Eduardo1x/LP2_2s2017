from ex03 import common_end
 

def test_ex03():
  print ('Common_end')
  assert common_end([1, 2, 3], [7, 3]) == True
  assert common_end([1, 2, 3], [7, 3, 2]) == False
  assert common_end([1, 2, 3], [1, 3]) == True
  assert common_end([1, 2, 3], [1]) == False
  assert common_end([1, 2, 3], [2]) == False


