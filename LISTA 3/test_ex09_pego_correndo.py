from ex09 import pego_correndo



 
def test_ex09():
  print ('Pego correndo')
  assert pego_correndo(60, False) == 0
  assert pego_correndo(65, False) == 1
  assert pego_correndo(65, True) == 0
  assert pego_correndo(80, False) == 1
  assert pego_correndo(85, False) == 2
  assert pego_correndo(85, True) == 1
  assert pego_correndo(70, False) == 1
  assert pego_correndo(75, False) == 1
  assert pego_correndo(75, True) == 1
  assert pego_correndo(40, False) == 0
  assert pego_correndo(40, True) == 0
  assert pego_correndo(90, False) == 2

 
