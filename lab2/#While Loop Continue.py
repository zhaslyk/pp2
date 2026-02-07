#While Loop Continue
#-------------------------------------------
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
#-------------------------------------------
i = 0
while i < 6:
    i += 1
    if i % 2 == 0:
        continue
    print("Odd:", i)
#-------------------------------------------
i = 0
while i < 10:
    i += 2
    if i == 6:
        continue
    print("Value:", i)
#-------------------------------------------
i = -3
while i < 3:
    i += 1
    if i == 0:
        continue  # Skip zero
    print("Non-zero:", i)
#-------------------------------------------
idx = -1
while idx < 4:
    idx += 1
    if idx == 1 or idx == 3:
        continue
    print("Index:", idx)
#-------------------------------------------