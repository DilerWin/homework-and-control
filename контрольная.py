#1-ая задача
length_1=float(input("Введите длину 1-ого параллепипеда: "))
width_1=float(input("Введите ширину 1-ого параллепипеда: "))
height_1=float(input("Введите высоту 1-ого параллепипеда: "))

length_2=float(input("Введите длину 2-ого параллепипеда: "))
width_2=float(input("Введите ширину 2-ого параллепипеда: "))
height_2=float(input("Введите высоту 2-ого параллепипеда: "))

volume_1=length_1*width_1*height_1
volume_2=length_2*width_2*height_2
if volume_1>volume_2:
    print("Больший обьем у 1-ого параллепипеда")
else:
    if volume_1 == volume_2:
        print("Обьемы равны")
    else:
        print("Больший обьем у 2-ого параллепипеда")


#2-ая задача
def сравнение():
    return k<=n

k = float(input("Введите число k: "))
n = float(input("Введите число n: "))

if k <= n:
    if k < n:
        print("k меньше чем n")
    else:
        print("k равно n")
else:
    print("Ошибка")




