#PYTHON 01
'''
this is comment
'''


n = 78000
last = 0
man5 = 50000
man1 = 10000
cheon5 = 5000

a=n//man5
print("5만원")
print(a)
last = n%man5
a=last//man1
print("만원")
print(a)
last=last%man1
a=last//cheon5
print("5천원")
print(a)
last=last%cheon5
a=last//1000
print("천원")
print(a)
