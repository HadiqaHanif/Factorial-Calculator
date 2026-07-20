#UserData
n = int(input("Enter a number: "))
#DicisionMaking
if n < 0 :
    print("Factorial is not defined for negative numbers.")
elif n == 0 :
    print("Factorial is: 1")
else:
    factorial = 1
    for i in range(1, n + 1):
        factorial = factorial * i
    print("Factorial is:", factorial)

