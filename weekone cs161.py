#Erica Skoog
#cs161
#Week one homework
from hmac import digest

#1
#setting my pet type and name as two variables
pet_type = "dog"
pet_name = "Posey"
print(f"I have a {pet_type} and her name is {pet_name}.")

#2
#asking for inputs
name = input("What is your name? ")
age = input("Enter your current age: ")
#convert entered number input into an integer to use in an f-string
age = int(age)
savings = input("Enter your saving yearly savings: ")
#convert entered number into an integer to use in an f-string
savings = int(savings)

print(f"Hello " + name +f"! You are currently {age} years old. In 10 years, you will be "+(str(age + 10))+f" years old. If you save {savings} each year, in 5 years you will have saved $" + str(savings*5)+". Your average monthly savings is $" + str(savings/12)+".")

#3
#need to enter an equation to get the amount of minutes in a month without doing the math
jan = str(31*(60*60*24))
print(f"The number of seconds in January is {jan}")

#4
eggs = input("How many eggs do you have?: ")
#convert the input to an integer
eggs = int(eggs)
#add two different equations one to find out how many dozen and one that finds the remainder
dozens = eggs//12
remaining = eggs%12
print(f"This makes {dozens} dozen eggs with {remaining} left over.")
