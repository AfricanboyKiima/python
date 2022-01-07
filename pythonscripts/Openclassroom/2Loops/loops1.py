#Started to look at loops this time a loop enables us to repeat instructions a certain number of times and we can as well specify the conditions as well
#...a certain number of times.
"""
NOTE
It is possible to use a loop to extract each character in a string since a string is a series of characters as well
"""
number = input("Insert the number to be multiplied : ")

number = int(number)
i = 1

print( 1 * number)
print( 2 * number)
print( 3 * number)
print( 4 * number)
print( 5 * number)
print( 6 * number)
print( 7 * number)
print( 8 * number)
print( 9 * number)
print( 10 * number)

print("#####################")

while i < 11:
    print(i, "*", number, "=",   i * number)
    i+=1

