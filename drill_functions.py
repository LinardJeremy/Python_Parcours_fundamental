# def hello(name):
#     print(name)

# x = "jeremy"

# hello(x)
# listOfStudent = ['jeremy',"tom","Christophe"]
# def sumOfStudent(list):
#     print((len(list)))

# sumOfStudent(listOfStudent)

# def is_divisible(n,x,y):
#     divisible_one = n % x
#     divisible_two = n % y
#     if divisible_one == 0 and divisible_two ==0:
#         return print(True)
#     else:
#         return print(False)

# is_divisible(3,1,3)
# is_divisible(12,2,6)
# is_divisible(100,5,3)
# is_divisible(12,7,5)

# test = "sam harris"
# long_test = "this is a big test with a lot of words"

# def abbrevName(name):
#     x = name.split()
#     y = []
#     for i in range(len(x)):
#         y.append(x[i][0])
#     abbrev = ".".join(y)
#     abbrev_maj = abbrev.upper()
#     return print(abbrev_maj)
       
# abbrevName(long_test)
# x = [1,-4,7,12]
# def positive_sum(numbers):
#     y = []
#     for i in range(len(numbers)):
#         if numbers[i] >= 0:
#             y.append(numbers[i])
#     return print(sum(y))

# positive_sum(x)
# x = ['5', '0', 9, 3, 2, 1, '9', 6, 7]
# def sum_mix(arr):
#     new_list= map(int,arr)
#     return print(sum(new_list))

# sum_mix(x)

# def whatday(num):
#     if num <=0 or num > 7:
#         return "Mettre un nombre entre 1 et 7"
#     if num == 1:
#         return "Lundi"
#     if num ==2:
#         return "Mardi"
#     if num == 3:
#         return "Mercredi"
#     if num == 4:
#         return "Jeudi"
#     if num == 5:
#         return "Vendredi"
#     if num ==6:
#         return "Samedi"
#     if num ==7:
#         return "Dimanche"

# print(whatday(1))
# print(whatday(7))
# print(whatday(14))
# print(whatday(-7))

# def summation(number):
#     x = []
#     if number <= 0:
#         return print("nombre supérieur à 0 svp")
#     for i in range((number+1)):
#         x.append(i)
#     return print(sum(x))

# summation(8)

# def countSheep(number):
#     i =0
#     if number <= 0:
#         return print("valeur superieur à 0 svp")
#     elif number > 0:
#         while i < number:
#             i+=1
#             print(i, "sheep")

# countSheep(5)
# countSheep(-4)
# countSheep(14)

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    if exam > 75 and exam <=90 or projects >=5 and projects < 10:
        return 90
    if exam >50 and exam < 75 or projects >=2 and projects < 5:
        return 75
    else:
        return 0 

print(final_grade(95,1))
print(final_grade(1,11))
print(final_grade(-25,3))