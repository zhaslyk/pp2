#For Loop Continue
#-------------------------------------------
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
#-------------------------------------------
for i in range(6):
    if i == 3:
        continue
    print(i)
#-------------------------------------------
for i in range(1, 10):
    if i % 2 == 0:
        continue
    print("Нечетное:", i)
#-------------------------------------------
words = ["hi", "hello", "py", "python"]
for w in words:
    if len(w) < 3:
        continue
    print("Длинное слово:", w)
#-------------------------------------------
nums = [1, -2, 3, -4, 5]
for n in nums:
    if n < 0:
        continue
    print("Положительное:", n)
#-------------------------------------------