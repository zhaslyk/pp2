#Boolean Values 
#------------------------------------------------------
bool(0) #False
bool(1) #True
bool(-1) #True
print(bool(0))
print(bool(1))
#------------------------------------------------------
age = 16
is_adult = age >= 18
is_adult = bool(age >= 18)
print(is_adult)
#------------------------------------------------------
print(bool(0))
print(bool(""))
print(bool(" "))
print(bool([]))
print(bool(42))
#------------------------------------------------------
is_non_zero = bool(number)
is_non_zero = number != 0
print(is_non_zero)
#------------------------------------------------------
x = 0
print(bool(x or "hello"))
print(bool(x and "hello"))
#------------------------------------------------------