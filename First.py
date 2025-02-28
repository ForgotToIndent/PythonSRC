#to show different stuff with py compared to java and first class

print("Hello World!")
print('Hello World!') #single quote



num1, num2, num3 = 1, 2, 3
print(num1, num2, num3)

pragraph = """This is a paragraph of two line.
please write two lines, here"""
print(pragraph)

decimal = 11.3
stringLiteral = "Elegant"
many = [1, 2, 3.1, 4.5, 9]
print(type(decimal))
print(type(stringLiteral))
print(type(many))

#implicit data type conversion
floater = 3.1
inter = 4
theSum = floater + inter
print(theSum) #auto converts a data to another, lower to higher (int to float)
#explicit would be to use int() or float() or str()


#using sep and end in print()
print("purple", "orange", "green", sep=" & ", end=" are my favourite!\n")

#different operants (+ _ * / // % **)
print(2 ** 5)
print(26 % 3)
print(25 // 4) #removes decimal and rounds down

#e example - 2.302e+5 = move 5 decimal to right for positive(230200), 2.302e-5 move to left (00002302)

#rounding
balance = 100.10 * 3
print(balance)
print((round(balance, 2))) #can add a number e.g. round(balance, 2) shows 2 decimal points

#'m' is the alias used
import math as m #enables pow(num, pow), sqrt(munum), ceil(num), floor(num)
result1 = m.pow(2,5)
print(result1)
result2 = m.sqrt(36)
print(result2)
pie = m.pi
print(pie)

#user input (java scanner), always returns string data
yourName = input("What is your name?: ")
print("Welcome,",yourName)
#error can occur if input recieved is integer and intended for maths but it is saved as string (TypeError) solution:
x = 1
y = int(input("Enter a num: "))
z = x + y
print(z)
#use split() for multiple inputs at once
a, b, c = input("Enter 3 numbers: ").split(',') #split using a comma
a, b, c = (int(a), int(b), int(c)) #cant join data type change lines like ^^
total = a + b + c
print(total)


#join strings
fName = "Mujtaba"
lName = "Ansari"
fullName = fName + " - " + lName
#can also do: fullName = f"{fName}, {lName}""
print(fullName)

#string indexes
message = "Hello There!"
print(message[0],message[-1],message[3])
print(message[6:10])
print("=" * 20)
print("Nigger! " * 3)

#basic string methods: isalpha(), islower(), isupper(), isdigit(),
#startswith(str), endswith(str), lower(), upper(), title(), lstrip()
#rstrip(), strip()

#string format
animal = "cow"
item = "hose"
print("The {1} jumped over the {0}".format(animal,item))

