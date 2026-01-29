n = int(input("type your year: "))

if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0):
    print("LEAP")
else:
    print("COMMON")