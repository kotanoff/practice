# -*- encoding: utf-8 -*-
m = input("Enter month: ")
d = {"January": "1", "February":"2", "March":"3", "April":"4", "May":"5",
     "June":"6","July":"7", "August":"8", "September":"9", "October":"10",
     "November":"11", "Decemeber":"12"}
if (d.has_key(m)):
    print d[m]
else:
    print("Введите-ка реальный месяц, пожалуйста.")
