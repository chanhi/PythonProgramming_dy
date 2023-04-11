"""
array = []
array.append('a')
print(array[2:3])
array = [1,2,3,4,5,6,7,8]
print(array[0:3:1])
print(array[1:len(array):2])
print(array[2:6:3])
print(array[::-1])
arr1 = ['a', 'b', 'c']
arr2 = [1,2,3]
arr3 = [4,5,6]
arr2 = arr1
arr1.append('d')
print(arr2)
food = ['자장면', '짬뽕', '칼국수', '백반', '피자', '햄버거', '족발']
food.insert(2, '덮밥')
print(food)
food.remove('짬뽕')
print(food)
print(food.pop(4))
food.clear()
print(food)
food = ['자장면', '짬뽕', '칼국수']
desert = ['커피', '케이크', '마카롱']
print(food + desert)
food.extend(desert)
print(food)
arr = [i**2 for i in range(10) if i%2==1]
print(arr)
arr = ['hello' for i in range(10)]
print(arr)
"""
sports = ['축구', '야구', '농구', '배구']
num = [11, 9, 5, 6]
for i in range(4):
    print(sports[i], ':', num[i], '명')
arr1 = [sports, num]
for j in range(4):
    print(arr1[0][j], ':', arr1[1][j], '명')