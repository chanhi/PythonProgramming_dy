'''
def sumf(a, b):
    return a + b
def hello(name="nilu", you="alex"):
    print("hello", name)
    print("hello", you)

hello("james")
a, b = input("input:").split(" ")
sumf(a, b)

def mysum2(*num):
    result = 0
    for i in num:
        result += i
    return result
print("result", mysum2(1,2,3,4,5,6,7,8,9))
'''


