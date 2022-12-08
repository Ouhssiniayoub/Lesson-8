def func1(a):
    a[0], a[-1] = a[-1], a[0]
    return a
 
n = int(input('m = '))
a = list(map(int, input("одна строка, разделенная пробелом : ")))
 
print(a)
print(func1(a))