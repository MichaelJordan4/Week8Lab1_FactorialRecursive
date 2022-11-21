#Michael Jordan
#CIS261
#Week8Lab1 FactorialRecursive


def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    else:
        return num * factorial_recursive(num - 1)

def factorial_iterative(num):
    fact = 1
    for number in range(2, num+1):
        fact = number * fact
    return fact
 
def main():
    print ("Factorial results using an interative function")
    print("0! =", factorial_iterative(0))
    print("1! =", factorial_iterative(1))
    print("2! =", factorial_iterative(2))
    print("3! =", factorial_iterative(3))
    print("4! =", factorial_iterative(4))
    print("5! =", factorial_iterative(5))
    print ("Factorial results using a recursive function")
    print("0! =", factorial_recursive(0))
    print("1! =", factorial_recursive(1))
    print("2! =", factorial_recursive(2))
    print("3! =", factorial_recursive(3))
    print("4! =", factorial_recursive(4))
    print("5! =", factorial_recursive(5))

if __name__ == "__main__":
    main()

