def squirrel_play(temp, is_summer):   
  maior_temp = 90
  if is_summer:
    maior_temp = 100

  if temp >= 60 and temp <= maior_temp:
    return True
  else:
    return False