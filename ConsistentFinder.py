from time import sleep
from colorama import Fore, Back, Style, init

init()
print("These Script is made By Antar")

a1 = int(input("Enter a1 value of the polynomial: "))
a2 = int(input("Enter a2 value of the polynomial: "))
b1 = int(input("Enter b1 value of the polynomial: "))
b2 = int(input("Enter b2 value of the polynomial: "))
c1 = int(input("Enter c1 value of the polynomial: "))
c2 = int(input("Enter c2 value of the polynomial: "))


def consistentchecker(a1, a2, b1, b2, c1, c2):

    if a1/a2 == b1/b2 == c1/c2:
        print(Fore.GREEN, "Consistent")
        print(Fore.GREEN, "Infinite Solution ")
        print(Fore.GREEN, "The Line Will Coincide Each Other")

    elif a1/a2 != b1/b2:
        print(Fore.GREEN, "Consistent")
        print(Fore.GREEN, "Unique Solution ")
        print(Fore.GREEN, "The Line will Intersect at One Point")

    elif b1/b2 != c1/c2 or a1/a2 != c1/c2:
        print(Fore.GREEN, "InConsistent")
        print(Fore.GREEN, "No Solutions ")
        print(Fore.GREEN, "The Line Will be Paralel")

    else:
        print(Fore.RED, "Something went Wrong")
        exit()


consistentchecker(a1, a2, b1, b2, c1, c2)

print("Thank you Using Our Script")
print("Please visit our website : https://www.apk-center.in For Free & Latest Movies")

input('Hit enter to exit')
