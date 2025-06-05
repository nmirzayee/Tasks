i = 0
while i < 20:
    i += 2
    print (i)


i = 0
total = 0
while i <= 50:
    total += i
    i += 1
print (total)

correct_password = "admin123"
user_input = input("Enter your password  ")
while user_input != correct_password :
    user_input = input("Try again")
print("congrgulation")

square = 0
i = 1
for i in range(1, 10):
    i += 1
    square = i**2
    print (square)

list_words = ["apple","banana", "cherry", "orange", "carrot"]
for word in list_words:
    print(f"{word}-{len(word)} letter")

for i in range(1, 6):
    for j in range (1, 6):
        print (f"{i} * {j} =", i*j)

list_number = [5, 6, 7, 8, 9, 3]
total_number = sum(list_number)
maximum = max(list_number)
minimum = min(list_number)
print (total_number)
print(maximum)
print(minimum)

string_list = ["i", "we", "you","thet"]
string_list[1] = "updated"
print (string_list)

names = ["Ali", "Mahdi", "Hadi", "Ahmad", "Aziz"]
for word in names:
    if word[0] == "A":
        print (word)
