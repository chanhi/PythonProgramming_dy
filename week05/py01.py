'''
str1 = 'java c python kotlin'
print(
    str1.find('python'),
    str1.index('java'),
    str1.find('ruby')
)
str1 = 'a b c d'
str1.split() # ['a', 'b', 'c', 'd']
str2 = 'a,b,c,d'
str2.split() # ['a', 'b', 'c', 'd']
m, n, x, y = input(">>").split() #공백으로 구분하여 4개의 수 입력
a, b = 3, 4
print('{} + {} = {}').format(a, b, a+b)
print('{0} + {1} = {2}').format(a, b, a+b)
print('{1} + {2} = {0}').format(a+b, a, b)
print('{0:d} / {1:d} = {2:f}').format(a, b, a+b) # 3 / 4 = 0.75
hour = 9
if hour>24:
    print("one day have to 24 hours")
elif hour>12 and hour<24: 
    print("afternoon")
elif hour<12 and hour>0:
    print("morning")
else:
    print("night")
score = int(input("input score:"))
if score < 200:
    print("50만원")
elif score < 400:
    print("100만원")
else :
    print("1000만원")
count=0
for i in range(1, 11):
    count += i
else:
    print("for문 범위에서 벗어남")
    print("for문 조건에서 벗어난 것을 실행")
print(count)
n=1
while n<=5:
    print(n, end=' ')
    n += 1
else:
    print(f"\n 반복 while 종료 : n => {n}")
maxnum = 4
max_h = 140
more=True
cnt = 0
while more:
    height = float(input("height:"))
    if height > max_h:
        cnt += 1
        print(f'{cnt}명 들어가세요')
    else:
        print("you cant enter")
    if cnt == maxnum:
        more = False
else:
    print(f"{maxnum}명 모두 찼습니다. 다음 번에 이용하세요~")
'''
while True:
    str1 = input("input")
    if str1=="exit":
        print("exit")
        break
    else:
        if(str1 == "next"):
            print("next input")
            continue
        print(str1)
