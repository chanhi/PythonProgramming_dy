'''
print(type("hello"))
print(4)
print(3.14)
a, b, c = 15, 1, 7
print(a, b, c)
a, b = 20, 4
a += b
a /= b
a *= b
a -= b
a %= b
a **= b
print(a, b)
cel = int(input('cel:'))
fa = cel *9/5 + 32
print('섭씨:', cel, ',', '화씨:', fa )
cel += 3
fa = cel *9/5 + 32
print('섭씨:', cel, ',', '화씨:', fa )
planet = input('input planet')
rad = input(planet + 'radius')
radius = int(rad)
length = 2*3.14*radius
print(planet, 'radius:', radius)
print(planet, '둘레:', length)
myStr = "Monty Python"
print(len(myStr), myStr[:5], myStr[6:], myStr[6:12])
print(myStr[-6:0])
'''
value = input("xxx.xx:")
num = value.replace('.', '')
sum = 0
sum += int(num[0])
sum += int(num[1])
sum += int(num[2])
sum += int(num[3])
sum += int(num[4])
print('입력값:', value)
print('모든 자릿수 합:', sum)