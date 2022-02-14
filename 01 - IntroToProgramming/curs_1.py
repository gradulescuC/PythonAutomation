"""

Notions to cover:
- Variables (What is a variabile, what is it used for, how to initialize a variable)
- Input
- Print
- Format inside print
- Constants (What is a constant, what can we use it for, how can we declare it)
- Dunder methods
- Built-in Functions
- Immutability
"""

# There are two types of comments in python
#       - single line comment - marked by #
#       - multi-line comment - marked by three double quotes/single quotes on each side of the comment


"""1. Variables + print"""

# A variable is a rezerved memory space where we can store information
# Unlike other programming languages, in python a variable is created only when a value is assigned to it

# Exercise: Check if the user given as input is the same as the user stored in a specific variable

expectedUsr = 'Gabriela'
expectedPass = 'abcd'
expectedSold = 1000
user = input("Enter User ")
assert user==expectedUsr # assert evaluates of the evaluated expression is true. If not, it returns error and it stops the execution of the program

# Same exercise, more complicated

userName = input("Enter your username: ")
if len(userName) >= 6 and len(userName) <= 12: # Here we use an if statement which checks if the user is between 6 and 12 characters with the help of the len function
    print("Now enter your password")
    userPassword = input("Enter your password: ")
    if len(userPassword) >= 6 and len(userPassword) <= 12: # if the user is correct, we do the same thing with the password
        print("You are able to log in!!!")
    else:
        print("Incorrect password. Choose another.")
else:
    print("Incorrect username. Choose another.")

# Note: In order to find out more about a function, we can use CTRL+Click on the specific function

# Variables are case sensitive
# We can copy the value from a variable into another variable
# Example
user_5 = 100 # instruction for defining and initializing a variable
#print(uSer_5) #  This will not work because the variable name is case sensitive and the system will not recognise this name
score = user_5 # here we assign the value of user_5 to the variable calles 'score'
print(score)

# ------------------------------------------------------------------------------------------------------------

""" 2. Input from keyboard """
x = input("Enter the first number ") # We assign a value from the keyboard to the variable x
y = input("Enter second value ")
output = int(x) + int(y) #  we apply forced conversion (CAST) to a variable (by default the data type of the value given from the keyboard is String)
output = int(x) % int(y)  # the modulo function - useful when we check if a number is odd or even - it returns the remainder from the devision of x by y
x,y,z = 1,2,3 # we can declare and initialise three variables at the same time
print(z)
print(f"{x} with {y} is {output}") # The f in the front lets the system know that we are about to send some variables inside the text that should be read, not displayed as text

# ------------------------------------------------------------------------------------------------------------

""" 3. Formating in print"""

print(f"{x} with {y} is {output}")  #print with formating
print(f"{x} modulo {y} is {output}" )

# Alte exemple de formatare:
name = 'Johnny'
age = 55

print('Hi' + name + '. You\'re' + str(age) + 'years old') # Exemple without formating
                                                             # We wrote You\'re with the character  "\" called escape character
                                                                # because we wanted the system to consider the sigle quote as a character to be displayed on the screen,
                                                                     # not as the end of the text to be displayed
print(f'Hi {name}, You are {age} years old') # Example with formatting

# Before python 3, formating was done with the function .format
# Example:

print('Hi {}. You  are {} years old.'.format('Johnny',55)) # Here the brackets will be replaced sequantially with the values between parantheses
print('Hi {}. You  are {} years old.'.format(name, age))
print('Hi {new_name}. You  are {new_age} years old.'.format(new_name = 'sally', new_age=100)) # Here we defined in-line the values for name and age


# ------------------------------------------------------------------------------------------------------------

"""4. CONSTANTE"""

# Constant = memory space that cannot/should not change its value
# Constants are not supported by python, and that's why if we want to define something as a constant, as a convention we will use
                                        #capital letters so that people know that that is a constant
# Useful when generating all sort of utilities for automation, where we define test inputs that should not change their behaviour
# Ex: username, sleep between automation test steps (we can agree at project level the sleep time)

PI = 3.14

# ------------------------------------------------------------------------------------------------------------
"""5. Dunder methods -> DUNDER = Double underscore"""

# Examples of dunders:
_x = 7  # it specifies a variable considered through convention as PROTECTED (it cannot be used in other packages). It is NOT dunder
__x = 8 # Variables preceded by __ are dunders and are a way to define PRIVATE variables (they cannot be used outside the class).
                    # The dunders are usually python reserved, so it is not recommended to defined variables as dunders

#Example of dunders:
if __name__ == '__main__':  # It checks if the program is executed individually or it is called from another program
    print("Another module")
    a: int = 5 # We ca declare a variable also by explicitely declaring the data type
    b: str = 'Johny goes to school'
    print(type(a))
    print(type(b))
    #c = a + b -> Here it will return concatenation error because we cannot sum a numerical data type with a string data type
    c = str(a) + b # Here it will be ok because we did a CAST to string for the variable a
    print(c)
    print(a)

# ------------------------------------------------------------------------------------------------------------

""" 6. Built in functions """

greet = 'Hello'
print("Calculate the length of the string and print it entirely")
print(len(greet)) # The len function shows how many characters there are in a string
print(greet[0:len(greet)]) # Here we applied the concept of slicing, which means that we can 'cut' the text and display it in 'slices'
                              # In this case we specified that we want to display everything from the beginning of the string (position 0) until we go through the entire length of the string
quote = 'to be or not to be'
print("Display the string in capitals - we can use upper or capitalize")
print(quote.upper())
print(quote.capitalize())
print("Find the first instance of the word 'be' in the text stored in the variable 'quote'")
print(quote.find('be'))
print("Replace all the instances of 'be' with 'me'")
print(quote.replace('be','me'))
print(quote)
name = 'Andreea'
print("The type function can be used to display in the console the data type of a specific variable")
print(type(name))
name = 1
print(type(name))

# ------------------------------------------------------------------------------------------------------------
""" 7. immutability -> Immutable is the when no change is possible over time. 
In Python, if the value of an object cannot be changed over time, then it is known as immutable. 
Once created, the value of these objects is permanent. 
Also, when we replace the data in a variable we do not actually replace it, we point the same variable name to a different memory location
"""

print("Immutability example")
age = 42
print(id(age))  # Here it returned the id 140207831785040 (might be different on some other system/laptop/pc and might differ between runs)
print(type(age))
print(age)

print("We assign a new value to the variable, but it will actually not replace but define another memory to which the variable age will point")
age = 43
print(age)
print(id(age)) #  Here it returned the id 140207831785072 because we point towards some other address in the memory


selfish = 1
print(selfish)
# selfish[0] = '1212' # It will return error because we cannot replace part of the data in a variable

Selfish=[1,45,'test','andrada']
Selfish[0] = '1212' # This will work because selfish is no longer a variable but a list, and the list is not immutable
print(Selfish)

selfish = 'me me met'
#01234567
print(selfish[0])
print(selfish[7])

#[start]
print(selfish[1:])
#[start:stop]
print(selfish[0:8])
#[start:stop:stepover]
print(selfish[0:8:2])
#[-1]
print(selfish[:5])
print(selfish[::1])
print("Aici e " + selfish[-1])
print(selfish[-3])
print(selfish[::-1])
print(selfish[::-2])


    

















