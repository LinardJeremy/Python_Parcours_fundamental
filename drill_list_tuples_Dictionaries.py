translation = {
    "car" : "voiture",
    "tree" : "arbre",
    "red" : "rouge",
    "sky" : "ciel",
    "computer" : "ordinateur"
}
translation['green'] = "vert"
print(translation)

sentence = "I am the master of the world"
new_list = []

for x in sentence:
    new_list.append(x)
    for j in range(len(new_list)):
        if new_list[j] == ' ':
            new_list.pop(j)

print(new_list)

universalNumber =  "The_universal_number_is_42"
new = []

for x in universalNumber:
    new.append(x)
    for j in range(len(new)):
        if new[j] == '_':
            new.pop(j)

new_str = "".join(new)
print(new_str)

heroes = {"Superman" : "Clark kent", "Batman" : "Bruce Wayne", "Spiderman" : "Tony Parker" }

print(heroes.values())
print(heroes.keys())
heroes['Spiderman'] = "Peter Parker"
print(heroes)


price = {
    "laser sword" : 229.0,
    "Mitendo DX" : 127.30,
    "Linux cushion": 74.50,
    "Goldorak briefs":29.90,
    "Nextpresso station":184.60
}

x = sum(price.values())
print(x)
del price["laser sword"]

print(price)