#While Loop Break
#--------------------------------------
i = 1
while i < 10:
    if i == 5:
        break
    print(i)
    i += 1
#--------------------------------------
while True:
    print("This runs once")
    break
#--------------------------------------
n = 1
while n < 100:
    if n % 7 == 0:
        print("First number divisible by 7 is:", n)
        break
    n += 1
#--------------------------------------
pass_found = False
attempt = 1
while attempt <= 5:
    if attempt == 3:
        pass_found = True
        break
    attempt += 1
print("Found at attempt:", attempt)
#--------------------------------------
i = 0
while i < 10:
    print("Processing...")
    if i == 2:
        print("Error detected, stopping!")
        break
    i += 1