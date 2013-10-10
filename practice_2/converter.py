# -*- coding: utf-8 -*-
def zero():
    print """********
*      *
*      *
*      *
*      *
*      *
*      *
********"""

def one():
    print """       *
     * *
    *  *
   *   *
       *
       *
       *
       *"""

def two():
    print """********
       *
       *
       *
********
*       
*       
********"""

def three():
    print """********
       *
       *
       *
********
       *
       *
********"""

def four():
    print """*      *
*      *
*      *
********
       *
       *
       *
       *"""

def five():
    print """********
*       
*       
*       
********
       *
       *
********"""

def six():
    print """********
*       
*       
*       
********
*      *
*      *
********"""

def seven():
    print """********
       *
       *
       *
       *
       *
       *
       *"""

def eight():
    print """********
*      *
*      *
********
*      *
*      *
*      *
********"""

def nine():
    print """********
*      *
*      *
********
       *
       *
       *
********"""
options = {0 : zero,
           1 : one,
           2 : two,
           3 : three,
           4 : four,
           5 : five,
           6 : six,
           7 : seven,
           8 : eight,
           9 : nine,
}

symb = ""
f = 1
while f:
  symb = input("Введите цифру('Q' для выхода): ")
  if symb == "Q":
    f = 0
  elif type(symb) != int:
    print "Это не цифра"
  elif symb > 9 or symb < 0:
    print "Это не цифра"
  else:
    options[symb]()
