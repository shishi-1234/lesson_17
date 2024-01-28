import random
import hashlib
numbers = [1,2,3,4,5,6,7,8,100]
result = []
for num in numbers:
    if num > 5 and num<50:
        result.append(num)

print(result)

a = []
for i in range(1,15):
    a.append(i)
print(a)
result = filter(lambda num:num > 5 and num<50, numbers)
print(list(result))

result1 = [num for num in numbers if num > 5 and num<50]
print(result1)
chisla = [14, 88, 15, 66, 12, 41, 584]
result2 = []
for ch in chisla:
    if ch >12 and ch<500:
        result2.append(ch)
print(result2)
chisla1 = [num for num in chisla if num > 12 and num<500]
print(chisla1)

names = ['leo', 'max', 'kate', 'mag']
namesup = [name.upper() for name in names]
print(namesup)
namesm = [namee for namee in names if namee[0] == 'm']
print(namesm)

one = [1 if num > 5 else 0 for num in numbers]
print(one)
result011 = {random.randint(1, 100) for i in range(100)}
print(result011)
result012 = {i:i**2 for i in range(1,10)}
print(result012)
hash_objest = hashlib.md5(b'Hello World')
print(hash_objest.hexdigest())
