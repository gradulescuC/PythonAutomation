# Verifica daca userul dat de la tastatura este acelasi cu userul stocat intr-o variabila
"""expectedUsr = 'Gabriela'
expectedPass = 'abcd'
expectedSold = 1000
user = input("Enter User ")
assert user==expectedUsr"""

# Varianta mai complicata

"""userName = input("Enter your username: ")
if len(userName) >= 6 and len(userName) <= 12:
    print("Now enter your password")
    userPassword = input("Enter your password: ")
    if len(userPassword) >= 6 and len(userPassword) <= 12:
        print("You are able to log in!!!")
    else:
        print("Incorrect password. Choose another.")
else:
    print("Incorrect username. Choose another.")"""


#TODO -> Comparatia pentru password si sold de la tastatura prin consola
# ------------------------------------------------------------------------------------------------------------
# Basic Operators

"""x = input("Enter the first number ") // Atribuirea unei valori de la tastatura unei variabile
y = input("Enter second value ")
output = int(x) + int(y) // conversia fortata a unei variabile (by default de la tastatura se defineste string)
output = int(x) % int(y)  // functia modulo - util cand verificam daca un numar este par sau impar
x,y,z = 1,2,3
print(z)
print(f"{x} with {y} is {output}" )"""
# ------------------------------------------------------------------------------------------------------------

# Printarea cu formatare
"""print(f"{x} with {y} is {output}") // printarea cu formatare
print(f"{x} modulo {y} is {output}" )

Alte exemple de formatare: 
name = 'Johnny'
age = 55


print('Hi' + name + '. You\'re' + str(age) + 'years old') // Exemplu fara formatare
print(f'Hi {name}, You are {age} years old) // Exemplu cu formatare

Formatarea inainte de python 3 se facea cu functia .format:
Exemple:
print('Hi {}. You  are {} years old.'.format('Johnny',55))
print('Hi {}. You  are {} years old.'.format(name, age))
print('Hi {new_name}. You  are {new_age} years old.'.format(new_name = 'sally', new_age=100))
"""
# ------------------------------------------------------------------------------------------------------------
# Variabilele sunt case sensitive, si putem sa alocam valoarea de la adresa de memorie a unei variabile la adresa de memorie a altei variabile
"""
user_5 = 100
print(uSer_5) #nu va merge pentru ca numele variabilei este case sensitive
score = user_5
print(score)
"""

# ------------------------------------------------------------------------------------------------------------
# Constantele nu sunt suportate de python, motiv pentru care orice vrem sa definim ca si constanta
# in python va fi scrisa ca si conventie cu majuscule, pentru a anunta eventualele persoane care vor folosi codul
"""Constant = memory space that cannot change its value.
Useful when generating all sort of utilities for automation, where we define test inputs that should not change their behaviour
Ex: username, sleep between automation test steps (we can agree at project level the sleep time)

PI = 3.14
"""
# ------------------------------------------------------------------------------------------------------------
# Dunder methods -> DUNDER = Double underscore

"""Exemple de dunders:
_x = 7 #specifica o variabila ce nu poate fi folosita in alte module. Nu este DUNDER
__x = 8 -> Variabilele cu __ sunt rezervate pentru metode specifice python, si nu este recomandam sa definim variabile de tip DUNDER

Exemplu:
if __name__ == '__main__':  -> Verifica daca programul este executat individual sau este apelat dintr-un alt program
    print("Another module")
    a: int = 5
    b: str = 'Ana are mere'
    print(type(a))
    print(type(b))
    #c = a + b -> Returneaza eroare de concatenare
    c = str(a) + b
    print(c)
"""

# ------------------------------------------------------------------------------------------------------------
# Built in functions
"""
greet = 'Hello'
print(len(greet))
print(greet[0:len(greet)])
quote = 'to be or not to be'
print(quote.upper())
print(quote.capitalize())
print(quote.find('be'))
print(quote.replace('be','me'))
print(quote)
name = 'Andreea'
print(type(name))
name = 1
print(type(name))
"""
# ------------------------------------------------------------------------------------------------------------
#immutability -> Nu putem sa modificam doar o anumita pozitie intr-o variabila
"""selfish = 1
print(selfish)
selfish[0] = '1212'
print(selfish)

Selfish=[1,45,'test','andrada']
Selfish[0] = '1212'
print(Selfish)


selfish = 'me me me'
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
print(selfish[-1])
print(selfish[-3])
print(selfish[::-1])
print(selfish[::-2])
"""



















