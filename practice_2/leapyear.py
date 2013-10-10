def leap(y):
  if type(y) != int:
    print "You entered not a number."
  else:
    if y%400==0:
      print("It's a leap year.")
    elif y%100==0:
      print("It's a not leap year.")
    elif y%4==0:
      print("It's a leap year.")
    else:
      print("It's not a leap year.")
