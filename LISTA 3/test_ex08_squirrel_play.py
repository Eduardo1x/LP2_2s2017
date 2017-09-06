from ex08 import squirrel_play


def test_ex08():
  print ('squirrel_play')
  assert squirrel_play(70, False) == True
  assert squirrel_play(95, False) == False
  assert squirrel_play(95, True) == True
  assert squirrel_play(90, False) == True
  assert squirrel_play(90, True) == True
  assert squirrel_play(50, False) == False
  assert squirrel_play(50, True) == False
  assert squirrel_play(100, False) == False
  assert squirrel_play(100, True) == True
  assert squirrel_play(105, True) == False
  assert squirrel_play(59, False) == False
  assert squirrel_play(59, True) == False	
  assert squirrel_play(60, False) == True
 
