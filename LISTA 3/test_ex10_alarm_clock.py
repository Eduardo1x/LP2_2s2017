from ex10 import alarm_clock

def test_ex10():
  print ('Alarm Clock')
  assert alarm_clock(1, False) == '7:00'
  assert alarm_clock(5, False) == '7:00'
  assert alarm_clock(0, False) == '10:00'
  assert alarm_clock(6, False) == '10:00'
  assert alarm_clock(0, True) == 'off'
  assert alarm_clock(6, True) == 'off'
  assert alarm_clock(1, True) == '10:00'
  assert alarm_clock(3, True) == '10:00'
  assert alarm_clock(5, True) == '10:00'


