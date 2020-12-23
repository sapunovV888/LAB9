from lab9 import strochka
print('введіть діапазон випадкових чисел ')
k=int(input())
print('введіть кількість чисел рядка')
n=int(input())
s=strochka(k,n)
lst_n = []
lst = s.split()
for el in lst:
    lst_n.append(int(el))
lst_n.sort()
for el in lst_n:
    print(el, end=',')
