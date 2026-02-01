#Erica Skoog
#Week 4 assignment

#1
#def average(num1, num2, num3):
    #'''Take 3 numbers and return the average'''
    #return (num1 + num2 + num3)/3
#print(average(1, 2, 3))
#print(average(8, 12, 27))

#2
#print(average(1, 2, 3))
#print(average(8, 12, 27))

#def average(num1, num2, num3):
    #return (num1 + num2 + num3) / 3
#This will not return with an answer since it will try to print the average before the average is ever defined

#3
def average(num1, num2, num3):
    '''Take 3 numbers and return the average'''
    return (num1 + num2 + num3) / 3

print(average(1, 2, 3))
print(average(10, 12, 3))
#print(num1)
#It will return the average of the first two print statements but will have an error for num1 since num1 isn't defined as a value just an entry for a different defined value

#4
def dog_age(age):
    '''Takes the dogs age and prints out a string including the dog age and human age'''
    return (str(age) +" dog years is equivalent to " + str(24+((age-2)*4)) +" human years.")
print(dog_age(5))
print(dog_age(10))

#5

def car_value(price, age, type):
    '''With the price, age, and type of car, the function with calculate the current value of the car'''
    #change the type entry to lower case for the rest of the equations to run properly
    type = type.lower()

    if type == "german":
        rate = -0.05
    elif type == "japanese":
        rate = -0.07
    elif type == "italian":
        rate = 0.05
    else:
        print("Invalid car type")
        return

    value = price
    for _ in range(age):
        value += value * rate

    print(f"The value of {type} car will be ${value:,.2f} after {age} years.")
print(car_value(80000, 8, "italian"))

#6
def dog_calc(dog_age):
    '''Calculate the dogs age in human years based on user input'''
    human_age = 24 + ((dog_age - 2) * 4)
    return human_age
print("Dog's age calculator: ")
dog_name = input("What is your dog's name? ")
dog_age = float(input(f"How old is {dog_name}? "))

human_age = dog_calc(dog_age)
print(f"Your {dog_name} is {human_age:.1f} human years old")

#Extra Credit
def price_of_cone(scoops):
    '''Calculates the the price of an icecream cone based on scoops'''
    icecream_price = (scoops * 1.15) + 2.25
    return icecream_price
print("Ice cream price calculator: ")
scoops = int(input("How many scoops would you like? "))
total_price = price_of_cone(scoops)

print(f"A {scoops}-scoop cone will cost ${total_price:.2f}")
