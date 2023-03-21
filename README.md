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
+, -, *, /, %(나머지), //, **
