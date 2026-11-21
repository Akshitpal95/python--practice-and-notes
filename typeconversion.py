#type Conversion(by python) & Type Casting(by programer)

age = input("Enter your age: ")

new_age = int(age) + 1
print(new_age)

print(float(new_age))
print(bool(new_age))
print(str(new_age))

#Type Conversion
print(1 + 2.5) #implicit
#Type Casting
print(1 + int(2.999)) #explicit