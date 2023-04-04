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


#### 함수
- 내장함수
len(), eval(), int(), max() ...
- 사용자 정의 함수
```python
def fun_name(arg_name):
    print("this is function")
    return
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
```python
from random import randint
randint(1,5) #1~5사이의 임의의 정수 반환
```