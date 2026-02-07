#Short Hand If Else
#-------------------------------------------
a, b = 20, 10
if a > b: print("a is greater than b")
#-------------------------------------------
status = "Adult" if age >= 18 else "Minor"
print(status)
#-------------------------------------------
print("Positive") if 5 > 0 else print("Negative")
#-------------------------------------------
max_val = a if a > b else b
print(max_val)
#-------------------------------------------
x = 5
print("Big") if x > 10 else print("Small") if x < 10 else print("Ten")
#-------------------------------------------