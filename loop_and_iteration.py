i = 1
while i <= 10:
    print(i)
    i += 1

while True:
    n = int(input("give a integer > 0 : "))
    print("You have provided", n)
    if n > 0:
        break
print("correct answer")

for i in range(10):
    print("Start of iteration", i)
    print("Hello")
    if i == 2:
        break
    print("End of iteration", i)
print("After the loop")