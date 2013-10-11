# -*- encoding: utf-8 -*-
import math
def temp():
    str = input("Введите строку вида '<имя константы:точность>: ")
    dic = {"pi":math.pi, "e":math.e}
    a=str[:str.find(":")]
    b=int(str[str.find(":")+1:])
    print(round(dic[a],b))
    
temp()
