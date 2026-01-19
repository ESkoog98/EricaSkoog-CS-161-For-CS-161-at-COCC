#Erica Skoog
# Week 2 homework

#1
#Has a value and prints it in 3 different layouts
x = 31
print(x, bin(x), hex(x))

#2
#x is a value that won't work for this setup
#x = 1.825
#print(x, bin(x), hex(x))
#returns with an error because it's a float and not a whole integer
#commented out to skip after running to see the error
# part 2 of question 2
x = 18
print(x, bin(x), hex(x))

#3
#printing the assigned values as a variable
y = 0b1011
z = 0xA3
print(y, z)

#4
w = x + y + z
print('the sum is ' , w)

#compression
#naming variables and assigning values
orig_size = 112
dict_size = 10
comp_size = 87

#printing using f-strings to print in multiple lines and pull in different inputs
print(f"""
	Compressed text size: {comp_size}
	     Dictionary size: {dict_size} 
	               Total: {comp_size + dict_size}
	  Original text size: {orig_size}
	         Compression: {(orig_size - (comp_size + dict_size)) / orig_size:.2%}
""")
#when I used the equation in number 1 - (compressed text+Dictionary size)/ divided by original size I got 79% instead of 27.92%

#Extra Credit
x = (int(input("Enter a number between -128 and +127: ")))
#check if input is a valid number in the range
if x < -128 or x > 127:
    print("Invalid input")
#If input is valid it needs to be converted to an 8 bit number for both negative and positive integers
else:
    print(format(x & 0xff, '08b'))
