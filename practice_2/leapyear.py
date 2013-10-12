def leap(y):
  if type(y) != int:
    print "You entered not a number."
  else:
    if not y%400:
      print("It's a leap year.")
    elif not y%100:
      print("It's a not leap year.")
    elif not y%4:
      print("It's a leap year.")
    else:
      print("It's not a leap year.")
leap(1904)
leap(1900)
leap(1903)
leap(2013)
