#This is a guess the number game.

def collatz(number):
    #if number is even, print number // 2 and return this value
    if number % 2 == 0:
        return number // 2
    #if number is odd, return 3 * number + 1
    elif number % 2 == 1:
        return 3 * number + 1

print("Please write one integer value: ")

try:        #checks if input is integer
    value = int(input())

    while value != 1:
        print(collatz(value))
        value = collatz(value)
except:     #gives a error if input was not a integer
    print("Error: you need to insert a int number")
