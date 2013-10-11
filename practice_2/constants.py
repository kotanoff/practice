# -*- encoding: utf-8 -*-
import math
def temp():
    dic = {"pi":math.pi, "e":math.e}
    str = input("Введите строку вида '<имя константы:точность>: ")
    a=str[:str.find(":")]
    try:
        b=int(str[str.find(":")+1:])
    except:
        print('''Второй параметр - не число.
По умолчанию установлена точность: 2''')
        b=2
    if(dic.has_key(a) and b >= 0):
        print "%.{0}f".format(b) % dic[a]
        #print(round(dic[a],b))
    else:
        print "Ошибочка вышла"
    
temp()
