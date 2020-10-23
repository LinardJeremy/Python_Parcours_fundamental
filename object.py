
# x = 10 
# y = 10
# x+=1
# print(id(x), id(y))
# print(x is y)

person = ["James", "Bond", "007", "Secret agent"]
person2 = person

person += ["English"]
person2 += ["Man"]
print(id(person), id(person))
print(person, person2)