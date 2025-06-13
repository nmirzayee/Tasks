my_list = [10, 20, 30, 40]
my_iterator = iter(my_list)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))

for number in my_list :
    print(number)




x = 10

def variable():
    global x
    x = 5
    print (x)
variable()
print (x)


def add(a, b):
    return a+b

import math_utils
result = math_utils.add(2,3)
print (result)

import datetime

today = datetime.datetime.now()

print (today.strftime("%d - %m - %y"))

my_birthday = datetime.datetime(today.year, 7 , 23)
if my_birthday<today:
    print (datetime.datetime(today.year+1, 7, 23))

left_days = (my_birthday - today).days
print (left_days)


import math
print (math.sqrt(81))
print (math.pi)
print (math.floor(5.9))

import math

r = 5
area = math.pi*r**2
print (area)


import json

student = {
    "name": "Alice",
    "age": 20,
    "GPA": 3.7
}

json_data = json.dumps(student)
print("JSON string:", json_data)

import json

json_string = '{"course": "Python", "level": "beginner"}'
data = json.loads(json_string)

print("Course:", data["course"])
for i in range(1, 20):
    print(i * '*')

