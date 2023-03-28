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
```python

```
- split()
```python

```
- center(), strip()
```python

```
- format()
```python

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