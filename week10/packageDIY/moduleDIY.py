import random

def myfun():
    print("this is my own func")

def nrandom(start, end, n, duplicated=False):
    lst = []
    if duplicated:
        for _ in range(n):
            lst.append(random.randint(start, end))
    else:
        lst = list(random.sample(range(start, end+1), n))
    return sorted(lst)

if __name__ == "__main__":
    print(nrandom(1, 45, 6))
    print(nrandom(1, 45, 6, True))