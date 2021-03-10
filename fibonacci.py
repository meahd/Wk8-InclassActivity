#David Meah - CS362 - Wk8 Inclass Activity

def Fibonacci(n):
    if n < 0:
        print("Invalid Input")
    
    elif n == 0:
        return 0

    elif n == 1 or n == 2:
        return 1

    else:
        return Fibonacci(n-1) + Fibonacci(n-2)

def Factorial(n):
    if n == 1:
        return n

    else:
        return n * Factorial(n-1)
       
#Driver code
print("8th Fibonacci Number is = ",Fibonacci(8))
print("Factorial of 7 is = ",Factorial(7))