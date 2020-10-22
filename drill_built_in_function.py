import math
countAlpha = len("Hello World!")
print(countAlpha)
countFloat = float(countAlpha)
print(countFloat)
roundPi = round(math.pi,(-10**2))
print(roundPi)
reversedText = reversed("Hello world")
print(reversedText)
for x in reversedText:
    print(x)

age = input("quel est votre age ? ")
print(age)
print(type(age))


num = [2, 8, 1, 4, 6, 3, 7]
sortNum = sorted(num)
print(sortNum)
sumOfList = sum(num)
print(sumOfList)

minValue = min(num)
print(minValue)

maxValue = max(num)
print(maxValue)

calc  = "1 + 2"
print(eval(calc))


