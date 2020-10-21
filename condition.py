age = 16
if age>=18:
    print("Tu es un adulte!")
elif age==15:
    print("Tu n'es pas un adulte!")
else:
    print('lOL')

student_1 = "Jemy"
student_2= "Tom"

if student_1 =="Jeremy" and student_2=="Tom":
    print("Vous êtes Tom et Jeremy")
else:
    print("Vous n'êtes pas les bons étudiants!")

if student_1 =="Jeremy" or student_2=="Tom":
    print("Vous êtes Tom et Jeremy")
else:
    print("Vous n'êtes pas les bons étudiants!")

student_list = ["Jeremy","Tom", "Patrick","Michel"]
student_to_find = "Jimmy"

if student_to_find in student_list:
    print("il est bien ici")
else:
    print("Il n'est pas ici")

if student_to_find not in student_list:
    print("il n'est pas ici")
else:
    print("Il est dans la liste")

x = 12
y = 10

if x is y:
    print("c'est les mêmes")
else:
    print("c'est pas les mêmes")