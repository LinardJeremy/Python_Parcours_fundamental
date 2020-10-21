import math
age = 42
age += 10
divAge = age // 7 
print(divAge)
textDiv = "{} diviser par 7 is equal to, {}" .format(age, divAge)
print(textDiv)
restDiv = age % 7
expDiv = restDiv**3
# # x= input()
# print(x)
# print(type(x))
milk_bottle = 0.45
cider_bottle = 3.85
flour_bag = 0.90
butter_packet = 0.77
nutella_jar = 1.87

orderPrice = (milk_bottle*2)+(cider_bottle*3)+flour_bag+butter_packet+nutella_jar
orderPrice = round(orderPrice,2)
print(orderPrice)
allowanceMoney = 20
allowanceMoney = allowanceMoney-orderPrice
if allowanceMoney>0:
    print("Vous avez dépensé {} il vous reste {}" .format(orderPrice,allowanceMoney))
elif allowanceMoney == 0:
    print("il ne te reste rien")
else:
    print("sorry, tu n'as pas assez d'argent il te manque {}" .format(abs(allowanceMoney)))

y = int(input())
z = int(input())


if y < z:
    print("La plus petite valeur est {}" .format(y))
elif z < y:
    print('La plus petite valeur est {}' .format(z))
elif z == y:
    print("les nombres sont identiques")

text1 = input()
text2 = input()

if text1 > text2:
    print("Le plus grand mot est {}" .format(text1))
elif text2 > text1:
    print('Le plus grand mot est {}' .format(text2))
elif text1 == text2:
    print("les mots ont la même longueur")

devise = input("quel est la devise E ou $ ?")
montant = int(input("quel est le montant ? "))

if devise == "E":
    convertir = montant * 1.18525
    print("Votre montant en dollar est égale à {} dollar" .format(convertir))
elif devise == "$":
    convertir = montant * 0.8437
    print("Votre montant en euro est égale à {} euros" .format(convertir))


studentsTuring = ["Redouane", "Justine", "Ruben", "Edouard"]
name = "Justine"
if name in studentsTuring:
    print("Tu es un turing !")
elif name not in studentsTuring:
    print("Tu n'es pas un turing!")

volume = (math.pi*4) * (10**3)
print(volume)
