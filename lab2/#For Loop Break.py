#For Loop Break
#-------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
#-------------------------------------------
for i in range(10):
    if i == 3:
        break
    print(i)
#-------------------------------------------
numbers = [1, 5, 8, 12, 15]
for n in numbers:
    if n > 10:
        print("Первое число больше 10:", n)
        break
#-------------------------------------------
for char in "password123":
    if char.isdigit():
        print("Найдена первая цифра!")
        break
#-------------------------------------------
data = ["ok", "ok", "error", "ok"]
for status in data:
    if status == "error":
        print("Цикл прерван из-за ошибки")
        break
    print("Статус:", status)
#-------------------------------------------