"""tu1 = 1,2,3,
print(type(tu1))

dict1 = {
    1:"1월",
    2:"2월",
    3:"3월",
    4:"4월",
    5:"5월",
    6:"6월",
    7:"7월",
    8:"8월",
    9:"9월",
    10:"10월",
    11:"11월",
    12:"12월"
}
for i in range(1,13):
    print(dict1[i])

for key in dict1:
    print(key, dict1[key])

for key, value in dict1.items():
    print(f'{key}: {value}')
city = {'대한민국':'서울', '미국':'워싱턴DC', '일본':'도쿄'}
print(city.popitem())
"""

l1 = [1,2]
l2 = [3,4]
l3 = [5,6]

l4 = zip(l1, l2, l3)
print(type(l4))

for i in l4:
    print(i[0], i[1], i[2])

title = ['한식', '양식', '중식', '분식']
food = ['불고기', '파스타', '짜장면', '떡볶이']

clist = list(zip('ABCD', title, food))
cdict = dict(zip(title, food))
print(cdict)
print(clist)