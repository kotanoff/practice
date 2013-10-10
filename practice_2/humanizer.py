#!/usr/bin/env python
# -*-coding: UTF-8 -*-
dic =  {'one':'час', 'two':'часа', 'many':'часов'}
def hum(n, dic):
  if type(n) != int:
    print "Enter an integer"
  elif type(dic) != dict:
    print "This isn't a dictionary"
  else:
    if(n % 10)==1:
        if (n%100)==11:
            print str(n) + " " + dic['many']
        else:
            print str(n) + " " + dic['one']
    elif (n % 10)>1 and (n % 10)<5:
        if n>=11 and n<=15:
            print str(n) + " " + dic['many']
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
hum(111, dic)
hum(131, dic)
hum(11111, dic)
