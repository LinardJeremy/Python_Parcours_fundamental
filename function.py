# def hello():
#     print("hello")

# hello()

# def hello(name): # <- Parameter
#     print("Hello {} and welcome".format(name))
    
# hello("Alan") # <- Argument

# def increaseMe(a):
#     return a + 2

# print(increaseMe(1))


# name = {}
# name["firstName"] =  "Alan"
# name["lastName"] = "Turing"

# def hello(firstName, lastName):
#     print("Hello {} {} and welcome".format(firstName, lastName)) 
    
# hello(**name)


# def hello(name = "Anonymous"): # <- Parametre
#     print("Hello {} and welcome".format(name))
    
# hello("jeremy")


# def multiply(*elements): # Add "*" to indicate that the parameters are infinite
#     res = 1
#     for element in elements:
#         res = res * element
#     return res
# print(multiply(1,2,3,4))

def doubleStuff(aList):
    """ Overwrite each element in aList with double its value. """
    for position in range(len(aList)):
        aList[position] = 2 * aList[position]

things = [2, 5, 9]
print(things)
doubleStuff(things)
print(things)