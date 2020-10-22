# students =  ["Merouane", "Baptiste", "Caroline", "Joe", "Sophie", "Nathan", "Raphaël", "Axel", "Mathieu", "Adrien"]

# for x in sorted(students):
#     print(x)

# for x in students:
#     if x[0]=="M":
#         print("prenom qui commence par M :",x)

# for i in range(1,15):
#      print(i)

# for i in range(1,10):
#     print(i)
#     if i == 5:
#         break
# print("la loop s'arrête à ", i)

# for i in range(1,10):
#     print(i)
#     if i < 5:
#         continue
#     print("Une nouvelle boucle commence quand on arrive à 5")
#     for i in range(1,10):
#             print("New boucle ",i)

# listOfnum = [17, 38, 10, 25, 72]

# for i in sorted(listOfnum):
#     print(i)
# listOfnum.append(12)
# for i in listOfnum:
#     print(i)
# for i in reversed(listOfnum):
#     print("reverse list of num",i)

# print(listOfnum[0])

# listOfnum.remove(38)
# print(listOfnum[1:3])
# print(listOfnum[:3])
# print(listOfnum[3:])
# print(listOfnum[-1])

# user_number= int(input("Entrez un nombre entier"))

# for i in range(0,(user_number+1)):
#     print(i)

# price = 42
# user_guess = int(input("Quel est le prix ?"))

# while user_guess != price:
#     if user_guess > price:
#         print("le prix est plus bas")
#         user_guess = int(input("Quel est le prix ?"))
#     elif user_guess < price:
#         print("le prix est plus élevé")
#         user_guess = int(input("Quel est le prix ?"))
#     if user_guess == price:
#         break
# print("C'est le bon prix tu as won!")   

# allStudents =  [["David", "Justine", "Valentin","Axel", "Redouane"], ["Julie", "Stéphane", "Mostapha", "Claudiu", "Son"]]

# for i in range(len(allStudents)):
#     for j in range(len(allStudents[i])):
#         print(allStudents[i][j], end=' is a alumni, ')
#     print()

languages = [["PHP", "Java", "C#"], ["HTML", "CSS", "Javascript"]]
for i in range(len(languages)):
    for j in range(len(languages[i])):
        if i == 0:
            print(languages[i][j], end=" is back end language ")
        elif i == 1:
            print(languages[i][j], end= " is front end language ")
    # print()
