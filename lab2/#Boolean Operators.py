#Boolean Operators
#----------------------------------------
print("=== Булевы операторы в Python: and, or, not ===\n")

print("True  and True  →", True and True)     # True
print("True  and False →", True and False)    # False
print("False and True  →", False and True)    # False
print("False and False →", False and False)   # False
print()

print("True  or True  →", True or True)       # True
print("True  or False →", True or False)      # True
print("False or True  →", False or True)      # True
print("False or False →", False or False)     # False
print()

print("not True  →", not True)                # False
print("not False →", not False)               # True
print()

print("5 and 0     →", 5 and 0)               # 0
print("5 and 18    →", 5 and 18)              # 18
print('"" or "hi"  →', "" or "hi")            # hi
print("0 or 7      →", 0 or 7)                # 7
print('"python" or 42 →', "python" or 42)     # python
#----------------------------------------
n = int(input("how old are u? "))
p = input("passport? yes/no ").lower() == "yes"

v = age >= 18 and has_passport

print("can vote:", can_vote)
#----------------------------------------
n = int(input("Введи число: "))

od = not (number % 2 == 0)

print("Число нечётное:", is_odd)
#----------------------------------------
m = int(input("Сколько денег? "))
t = int(input("Какая температура? "))

cd = money >= 200 and temp > 20

print("Можно купить мороженое:", can_buy_icecream)
#----------------------------------------
n = input("Какой сегодня день недели? ").lower()

b = day == "суббота" or day == "воскресенье" or day == "пятница"

print("Сегодня выходной или пятница?", b)
#----------------------------------------