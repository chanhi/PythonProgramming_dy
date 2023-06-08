# PYTHON
## Python Programming
* donyang study note

[<img src="imgs/pythonlogo.webp" width="100px"><br>python.org ](https://www.python.org/)

<hr/>

### Github
#### git commit
* git init
* __git config --global user.email "your@email.com"__
* git add .
* git commit -a -m "your commit"
* git log
#### git으로 레퍼지토리 연결
* git remote add origin http://yourRemote.git
* git remote -v  ->  check remote server
* git push origin master
#### master -> main
* git branch -M main
* git push origin -u main
* git checkout -t [external branch] -> 클론된 레파지토리에서 브런치를 가져옴
#### 레퍼지토리 git으로 clone하기
* git clone [repository_url]
* git clone -b branchName [repository_url]
#### update to local from remote
* git pull
* git fetch
* git merge
#### git branch
* git branch -> current branch
* git branch new_branch -> create new branch
* git checkout new_branch -> move branch
* git merge new_branch -> merge new_branch to current branch 

<hr/>

### Python

#### 자료형
```python
"문자열" #string
23 #int
3.14 #float
True # Boolean
[1, 2, "num"] #array
(1, 2, "num") #tuple
{"key": "value", "key": ["value", "arr"]} #dictionary
```

#### 리스트(list)
- 대괄호[]로 리스트를 구성
- 값은 정수, 실수, 문자열, 리스트 등 모두 가능
```python
array1 = [1, '2', 'string', [1,2,3]]
array2 = [] #빈 리스트 생성
array3 = list() #빈 리스트 생성
array2.append('add') #리스트의 가장 뒤에 항목 추가
array2.insert(0, 'insert') #첫 인자의 인덱스 위치에 두번째 인자를 삽입 [(0)add(1)]
array1[len(array1) - 1] = 2 #인덱싱, 해당하는 값이 없으면 IndexError: list index out of range
array1[0:2] #슬라이싱, 해당하는 값이 없으면 빈 리스트 반환
print(array1[3][0]) #1 반환
array1.remove('2') #해당 값을 삭제, 없으면 ValueError 발생
popValue = array1.pop(0) # 인자값에 해당하는 index에 위치한 값을 제거하며 반환, 없으면 IndexError
```
- 여러 리스트 메소드
    - ```count()``` : 값을 가지는 항목의 수
    - ```index()``` : 해당 값이 위치한 첫번째 인덱스 반환 
    - ```reverse()``` : 순서를 뒤집음
    - ```sort()``` : 리스트 순서 정렬(default 오름차순, reverse=True=>내림차순 정렬)
- ```sorted(list)```: 리스트를 정렬한 리스트를 반환하는 함수(reverse=True=>내림차순)
- 리스트를 슬라이싱된 부분에 대입하면 배열이 아닌 값이 대입된다.
```python
array1 = [1,2,3,4,5,6]
array2 = [7,8,9]
array1[2:3] = array2[:1] # [1,2,7,8,5,6]
del array1[0:2] #해당 부분 삭제, 인덱스 전달은 필수, 없으면 에러발생
array1.clear() #빈 리스트로 만듦
array1 = ['월', '화', '수']
array2 = ['목', '금', '토', '일']
print(array1 + array2) # 두 리스트가 연결되 출력
array1.extend(array2) # array2가 array1에 연결됨
```
- 리스트에 * 연산자를 사용하면 그만큼 반복된 값이 추가
```python
arr=[1,2] 
arr*3 # [1,2,1,2,1,2])
```
- 조건을 만족하는 항목으로 리스트를 간결히 생성하는 컴프리헨션
```python
even = [i for i in range(2, 11, 2)] # 2~10까지의 짝수 배열
arr = [i**2 for i in range(10) if i%2 == 1] # 10 이하의 홀수의 제곱
```
- 리스트 대입에 의한 동일 리스트 공유
    - 얕은 복사(대입하는 변수가 동일한 시퀀스를 가리킴)
    - arr1 = arr2 라고 하면 arr1이 arr2를 지칭하게 됨. 
- 리스트 대입으로 새로운 리스트 생성
    - 깊은 복사(새로운 리스트를 만들어 복사)
    - ```copy(arr)``` 메소드 이용
    - ```arr1 = arr2[:]``` 슬라이싱 이용
    - ```list(arr)``` 함수 이용
- 피연산자인 변수 2개가 동일한 메모리를 공유하는지 검사하는 ```is``` (같으면 True, 다르면 False)
```python
f1 = [1,2,3,4]
f2 = f1 #얕은복사
print(f1 is f2) #True
f3 = list(f1) #깊은복사
print(f1 is f3) #False
```

#### 튜플(tuple)
- 괄호()로 튜플 구성
- 값은 리스트와 똑같이 뭐든 상관 없음
- immutable(수정불가능한) 속성을 가지고 있음(append, insert, 값 변경 등 불가)
- 값이 변경되는 메소드나 함수 이외에는 리스트와 같은 것을 가짐
- 항목이 하나인 튜플을 표현할 때는 마지막에 콤마를 반드시 붙임 ```tu = 1,```
```python
tup1 = (1,2,3)
tup2 = tup1 * 2 #(1,2,3,1,2,3)
tup1 += tup2 #(1,2,3,1,2,3,1,2,3)
del tup1 # tuple 삭제
tup3 = 1,2,3, #(1,2,3)
```

#### 딕션어리(dict)
- key:value 형태의 항목을 나열 ```<class 'dict'>```
- ```dict()``` 빈 딕셔너리 생성
```python
dict1 = {
    key1:value1,
    key2:value2
}
dict1[key3] = value3 #key3:value3 항목 추가
dic2 = dict([['월', 'Monday'],['화', 'Tuesday'],['수', 'Wednesday']])
dic2 = dict((['월', 'Monday'],['화', 'Tuesday'],['수', 'Wednesday']))
dic2 = dict([('월', 'Monday'),('화', 'Tuesday'),('수', 'Wednesday')])
dic2 = dict((('월', 'Monday'),('화', 'Tuesday'),('수', 'Wednesday')))
```
- 딕션어리 메소드
    - keys(): 키로만 구성된 리스트 반환
    - items(): (키, 값) 쌍의 튜플이 들어 있는 리스트 반환
    - values(): 값으로만 구성된 리스트 반환
    ```python
    day=dict(월='monday', 화='tuesday', 수='wednesday', 목='thursday')
    for key in day.keys():
        print(f'{key}:{day[key]}') #월:monday ...
    for key in day:
        print(f'{key}:{day[key]}') #월:monday ...
    for key, value in day.items():
        print(f'{key}: {value}') #월:monday ...
    print(day.values()) #monday, tuesday, ...
    ```
    - get(key, 해당 키가 없을 때 반환값): 키로 조회
    - clear(): 기존의 모든 키와 값을 삭제 -> 빈 딕셔너리
    - del dict_name: 딕셔너리 변수 제거
    ```python
    city = {'대한민국':'서울', '미국':'워싱턴DC', '일본':'도쿄'}
    city.get('대한민국', '없네요') # '서울', 만약 없어으면 '없네요' 출력
    city.clear() # {}
    del city # 변수제거
    ```
    - pop(키): 해당 키의 값을 반환하고 삭제
    - popitem(): 마지막으로 삽입된 키의 (키, 값) 튜플을 반환하고 삭제
    - update(dict_name): 다른 딕셔너리와 병합(만약 같은 키값이 있다면 값만 변환)
    ```python
    city = {'대한민국':'서울', '미국':'워싱턴DC', '일본':'도쿄'}
    city.pop('일본') #'도쿄' 반환
    city.popitem() # ('미국', '워싱턴DC') 반환
    city2 = {'독일':'베를린'}
    city.update(city2) #city = {'대한민국':'서울', '독일':'베를린'}
    city.update({'대한민국':'부산'}) #city = {'대한민국':'부산', '독일':'베를린'}
    ```

#### list, tuple, dict 타입 변환
- list <-> tuple ```list()```와 ```tuple()```을 이용해서 변경
- zip(list1, list2): zip 클래스의 형태로 각 원소의 같은 인덱스의 값을 묶어 반환하는 함수
```python
l1 = [1,2]
l2 = [3,4]
l3 = [5,6]
l4 = zip(l1, l2, l3)
print(type(l4)) #<class 'zip'>
for i in list(l4):
    print(i[0], i[1], i[2])
#1 3 5
#2 4 6
title = ['한식', '양식', '중식', '분식']
food = ['불고기', '파스타', '짜장면', '떡볶이']
clist = list(zip('ABCD', title, food))
cdict = dict(zip(title, food))
print(clist)#[('A', '한식', '불고기'), ..., ('D', '분식', '떡볶이')]
print(cdict)#{'한식': '불고기', '양식': '파스타', '중식': '짜장면', '분식': '떡볶이'}
```
- list를 dict으로 만들어서 원하는 key값의 value를 출력하는 예제
```python
lec = ["python", "java", "c", "spring", "AI"]
lec_class = [101, 102, 103, 104, 105]
lecdict = dict(zip(lec, lec_class))
print(lecdict)

while(True):
    winput = input("lec:")
    if(winput == 'quit'):
        break
    for k, v in lecdict.items():
        if(winput == k):
            print(f'{k}: {v}')
        else:
            print("you input unable value. write again")
```

#### 연산식
- 연산자
+, -, *, /, %(나머지), //, **
- 대입연산자
=, +=, -=, *=, /=, %=, **=, //=


#### 문자열(str)
```python
"큰따음표 문자열"
'작은따음표 문자열'
"he's developer"
'this is "python"'
"""
여러 문자열
"""
```


#### 문자열 관련 메소드
- replace() : 문자 치환
    - 문자열의 immutable(수정될 수 없는) 속성 때문에 이러한 메소드들은 새로운 문자열을 반환함
```python
str1 = "this is a test string."
str2 = str1.replace('this', 'that') #"that is a test string."
str1.replace('i', 'k', 2) #"thks ks a test string" -> 지정횟수만큼 치환
print(str1) #"this is a test string -> immutable 속성(수정 불가)
print(str2) #"that is a test string."
```
- count() : 지정 문자열 출현 횟수, join() : 원하는 문자열을 문자와 문자 사이에 삽입
```python
str1 = '내가 그린 기린 그림은 니가 그린 기린 그림보다 더 나은 기린 그림이다'
str1.count('기린') # 3반환
str2 = '12345'
str2.join(,) #"1,2,3,4,5"
```
- find(), index()
    - 찾고자 하는 문자열의 첫 번째 인덱스를 반환
    - find() : 없으면 -1 반환
    - index() : 없으면 ValueError
```python
str1 = 'python java c js'
str1.find("java") #7
str1.index('python') #0
str1.find('ruby') # -1
```
- split()
    - 문자열을 특정한 기준으로 분리
```python
str1 = 'a b c d'
str1.split() # ['a', 'b', 'c', 'd']
str2 = 'a,b,c,d'
str2.split() # ['a', 'b', 'c', 'd']
m, n, x, y = input(">>").split() #공백으로 구분하여 4개의 수 입력
```
- strip()
    - 문자열 앞뒤의 특정 문자들을 제거
```python
'  python  '.lstrip()#'python  '
'  python  '.rstrip()#'  python'
'  python  '.strip()#'python'
'**python--'.strip('* -')#'python'
```
- format()
```python
a, b = 3, 4
print('{} + {} = {}').format(a, b, a+b)
print('{0} + {1} = {2}').format(a, b, a+b)
print('{1} + {2} = {0}').format(a+b, a, b)
print('{0:d} / {1:d} = {2:f}').format(a, b, a+b) # 3 / 4 = 0.75
```
- formating의 다른 방식
```python
a = 7
print(f'number: {a}')
```


#### 이스케이프 시퀀스
\\, \', \", \n ...
```python
print("\"hello\nworld\"")
```
```
"hello
world"
```


#### 인덱싱(indexing), 슬라이싱(slicing)
- 문자열, 배열 등에 사용
- 인덱스의 첫번째는 0
- 길이를 벗어나는 인덱스 참조는 오류(IndexError:index out of range)
```python
myStr = "Hello World!"
arr = [1, 3, 5, 7, 9]
#indexing
print(myStr[0], arr[1], arr[-1], myStr[len(myStr)//2])
#slicing
print(myStr[:5], arr[2:4], arr[1, -2])
#step
print(myStr[1:9:3], arr[::-1], arr[::1]) #범위 안에 간격마다 출력/ 역순 출력/ 정순 출력
```


#### bool 자료형
- True, False
- type: class 'bool'
- 0과 ''일때 False, 나머지 값이 있는 경우 True
- ```bool()``` : 값에 따라 True와 False를 반환
- 관계연산자
 - \>, >=, <, <=, ==, !=


#### 표준입력
```python
a = input('입력메세지')
res = int(a) + 3
```
- 기본적으로 str 타입으로 받는다
- 자료변환 함수(str(), int(), float())를 이용해 원하는 타입으로 변경

#### 집합
- 중복되는 요소가 없으며 순서도 없는 원소의 모임
- 원소는 불변의 값이고 중복될 수 없으며 유일하다. 순서는 의미가 없다.
- {1, 4, 6, 7}, {(1,1), (2,5), (3, 4)}
```python
odd = {1,3,5}
odd.add(7) #{1, 3, 5, 7}
odd.remove(3) #{1, 5, 7} -> 해당 key가 없으면 오류 발생
odd.discard(3) #{1, 5, 7} -> 해당 key가 없으면 아무것도 실행 안함
odd.pop() # 맨 앞 원소 1반환
odd.clear() # 빈 집합으로 만듦
```
- 합집합
```python
a = {3, 6, 9, 12}
b = {4, 6, 8, 10, 12}
a | b # {3,4,6,8,9,10,12}
a.union(b) #{3,4,6,8,9,10,12} 리턴(a, b 변경 x)
a.update(b) #{3,4,6,8,9,10,12}로 a를 업데이트
```
- 교집합
```python
a = {3, 6, 9, 12}
b = {4, 6, 8, 10, 12}
a & b # {12, 6}
a.intersection(b) #{12, 6} 리턴(a, b 변경 x)
a.intersection_update(b) #{12, 6}로 a를 업데이트
```
- 차집합, 여집합
```python
a = {3, 6, 9, 12}
b = {4, 6, 8, 10, 12}
#차집합
a - b # {8, 10, 4}
a.difference(b) #{8, 10, 4} 리턴(a, b 변경 x)
#여집합
a ^ b #{3, 4, 8, 9, 10}
a.symmetric_difference(b) #{3, 4, 8, 9, 10}
```
-집합 연산의 축약 대입 연산자
```python
a |= b # = a.update(b)
a &= b # = a.intersection_update(b)
a -= b # = a.difference_update(b)
a ^= n # = a.symmetric_difference_update(b)
```

#### 함수
##### 내장함수
- len(), eval(), int(), max() ...
- map(function, iterable)
    - iterable의 항목들을 순서대로 functiond르 적용한 뒤 결과를 반환
    ```python
    def add (x, y):
        return x + y
    lst = list(map(add, [10, 30, 50, 20], [1, 3, 5, 2]))
    print(lst) # [11, 33, 55, 22]
    lst = list(map(lambda x, y: x + y, [10, 30, 50, 20], [1, 3, 5, 2]))
    print(lst) # [11, 33, 55, 22]
    ```


##### 사용자 정의 함수
```python
def fun_name(arg_name="default"): #인자 default값
    print("this is function")
    return arg_name + "return"

def subfunc(a, b): #위치인자
    return a - b

fun_name("arg") #함수의 호출은 함수 정의 이후에만 가능
subfunc(b=2, a=5) #키워드 인자 사용
```
- 전역변수, 지역변수
```python
i=20
a=2
def addOne():
    i=10
    global a # 글로벌 변수로 지정
    i += 1
    print(i)
def addTwo():
    print(i+2)
print(i) #20 전역변수
addOne() #11 지역변수
addTwo() #22 대입이 없는 경우 전역변수 참조
```
- 함수에서 값을 대입하지 않고 지역변수를 참조하면 오류
```python
i=20
def addone():
    print(i + 1)
    i += 1 #수정이 있으므로 지역변수로 인지, 참조할 i가 없으므로 오류
```
- 가변인자 *args
    - *은 리스트나 튜플을 unpacking해 가변 인자 형태로 변환
    - 예) print(1,3,5)
- 사전 형식의 키워드 가변인자 **kwargs
    - 키워드 형태 가변인자 전달 (key:value형태 등)
```python
def sumvalue(*values **kwargs):
    hap = 0
    for v in values:
        hap += v
    for key in kwargs:
        hap += kwargs[key]
    return hap

coffeeprice = {'value': 2000, '에스프레소': 2000, '아메리카노':2800, '카페라떼': 3200}
print(sumvalue(1,2,3, **coffeeprice)) # 10006
print(sumvalue(*[2,3,4], **coffeeprice)) # 10009
```
- 람다 함수(lambda function)
    - 작고 이름이 없는 함수
    - 키워드 lambda 이후에 콤마로 구분된 인자 목록
    - 람다 함수는 여러 개의 인자를 취할 수 있지만 표현식은 하나만 가능
    - return 없이 하나의 표현식 결과값 반환
```python
print((lambda x: x ** 3)(3)) # 27
print((lambda a, b: a%b)(10, 3)) # 1
div = lambda a, b: a/b
print(div(10, 2)) # 5.0
```


#### 조건문
```python
if true:
    print("콜론으로 블록 분리")
elif (a==b):
    print("else if는 elif로 표현")
else:
    print("위의 조건이 모두 아닌경우")
```


#### 반복문
- for
    - ```range([start, end, step])``` 이 내장 함수는 일정 간격의 정숫값 나열을 제공
    - 인자는 모두 정수여야 하고 start부터 end 이전 값 까지 step의 간격의 배열을 제공
```python
for i in range(10): #0~9
    print(i)
```
- while
```python
a=0
while(a != 7):
    input('a:')
    print('a not 7')
```
- continue, break
    - countinue: 다음 반복문을 시작
    - break: 반복문을 탈출함


#### 모듈 import
- module: 함수나 클래스 정의 등의 파이썬 코드가 저장된 소스파일
- third party modules: 여러 회사나 전문가가 개발해 배포하는 모듈
- 표준 module: 파이썬에 기본적으로 설치되는 모듈(random, math, datetime, sys, os -> sys.builtin_module_names에 모든 이름이 있음) 
- 사용자 지정 모듈: python 소스파일에 원하는 함수와 클래스 정의 후 import
- 패키지: 모듈을 모아둔 폴더
```python
import math
print(math.gcd(12, 16)) #4 최대공약수
print(math.trunc(3.141592)) #3 내림
print(math.fsum([1.2, 2.5])) #3.7 실수합
print(math.sqrt(4)) #2.0 제곱근
print(math.e) #자연수 e
print(math.pi) #원주율 pi
print(math.degrees(math.pi), math.radians(90)) #180.0, pi/2
print(math.floor(3.8), math.ceil(3.1)) #3, 4 내림, 올림
```

```python
from random import randint, choice, shuffle, sample #원하는 함수만 import하기 위해서 from 사용 *import random 하면 전부 import
randint(1,5) #1~5사이의 임의의 정수 반환
array = [1,2,3,4,5]
choice(array) #array 임의의 수 반환
shuffle(array) #array 순서 랜덤 변경
print(sample(array, 2)) #랜덤한 값 두개 출력
```
##### numpy, matplotlib
- numpy
    - ndarray: numpy의 기본 자료형(속도 빠름)
    - ndarray의 연산은 각 데이터가 서로 연산된다.
```python
import numpy as np
arrA = np.array([1,2,3,4,5])
arrB = np.array([5,4,3,2,1])
print(arrA + arrB) #[6 6 6 6 6]
arrA.shape #(5,)
arrC = np.array([[1,2],[3,4],[5,6]])
arrC.shape #(3,2)
```

- matplotlib
    - 데이터를 시각화하는 라이브러리
    - 라인 플롯, 바 차트, 파이 차트, 히스토그램, 박스 플롯, 스태커 플롯 등
    - 10주차 [data_visualiztion.py](week10/data_analysis/data_visualization.py) 여러가지 시각화
    - folium 라이브러리를 통해 지도에 시각화 가능
```python
from matplotlib import pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s = 1 + np.sin(2 * np.pi * t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='voltage (mV)',
       title='About as simple as it gets, folks')
ax.grid()

plt.show()
```

#### BeautifulSoup
- ```from bs4 import BeautifulSoup as bs```
- 웹의 정보를 크롤링 하기 위한 라이브러리
- requests: 웹에 정보를 요청하고 받기 위한 라이브러리
```python
from bs4 import BeautifulSoup as bs
import requests

url = "https://naver.com"
result = requests.get(url)
soup = bs(result.text, "html.parser")
print(soup)
```


#### 내장변수
##### __name__
- 모듈 자체에서 시작되어 실행되면 __main__이 저장됨
- 다른 곳에서 호출되면 자신의 모듈 이름이 저장됨
```python
#helloWorld.py
def hello_world():
    print("hellow world")

if __name__ == '__main__' # 소스파일 자체를 실행하면 true, 소스파일을 모듈로 이용해 import 하면 false
    print("이 실행 결과는 이 파일을 실행했을 때 출력됩니다.")
    print("만약 import되어 이 소스파일이 이용될 땐 출력되지 않습니다.")
```
```python
#main.py
from helloWorld improt hello_world
hello_world() #hellow world
```
