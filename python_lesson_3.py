'''AGE CALCULATOR 
1)  calculate Age of a person - User should enter the year of birth and the program should output the age.. eg : entered value is 1990, 
output age is 30

2) Simple Calculator:
	- get 2 numbers from the user and print the result of addition, subtraction, multiplication and floor division, decimal division, remainder, 
	power of the input numbers
'''

name = input("Would you like to calculate your age? First tell us your name : ")
print("Hello" , name)
year = input("Which year were your born in? : ")
print(int(year))
age = (2021 - int(year))
print("You are", age, "years old!")

number_1 = input("Hello! What is the 1st number you would like to add as part of the calculation?: ")
number_2 = input("What other number would you like?:")

addition = int(number_1) + int(number_2) 
print("Addition answer is =" , int(addition))

subtraction = int(number_1) - int(number_2)
print("Subtraction answer is =" , int(subtraction))

multiplication = int(number_1) * int(number_2)
print("Multiplication answer is =" , int(multiplication))

division = int(number_1) / int(number_2)
print("Division answer is =" , int(division))

remainder = int(number_1) // int(number_2)
print("Remainder answer is =" , int(remainder))

power = int(number_1) ** int(number_2)
print("Powered answer is =" , int(power))