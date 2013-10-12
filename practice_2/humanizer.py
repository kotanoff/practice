#!/usr/bin/env python
# -*-coding: UTF-8 -*-
dic =  {'one':'час', 'two':'часа', 'many':'часов'}
def hum(n, dic):
  if type(n) != int:
    print "Enter an integer"
  elif type(dic) != dict:
    print "This isn't a dictionary"
  else:
    if n%10 in range(1,5):
        if n%100 in range(11,15):
            print str(n) + " " + dic['many']
        elif(n % 10)==1:
            print str(n) + " " + dic['one']
        else:
            print str(n) + " " + dic['two']    
    else:
        print str(n) + " " + dic['many']
    
hum(1, dic)
hum(2, dic)
hum(5, dic)
hum(10, dic)
hum(11, dic)
hum(12, dic)
hum(14, dic)
hum(17, dic)
hum(21, dic)
hum(22, dic)
hum(112, dic)
hum(132, dic)
hum(11111, dic)
