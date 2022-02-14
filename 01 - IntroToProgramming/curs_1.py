"""

Notiuni de acoperit:
- Variabile (ce este o variabila, la ce foloseste, initializarea unei variabile)
- Input
- Print
- Formatarea in print
- Constante (ce este o constanta, la ce foloseste, cum se declara)
- Dunder methods
- Built-in Functions
- Immutability
"""

#  Comentariile in python sunt de doua tipuri:
#       - single line comment - marcat de #
#       - multi-line comment - marcat de trei ghilimele/apostroafe de o parte si de alta a comentariului


"""1. Variabile + print"""

# O variabila este o adresa de memorie la care sunt stocate anumite informatii
# Spre deosebire de alte limbaje de programare, in python o variabila nu e creata decat in momentul in care ii alocam o valoare

# Exercitiu: Verifica daca userul dat de la tastatura este acelasi cu userul stocat intr-o variabila

expectedUsr = 'Gabriela'
expectedPass = 'abcd'
expectedSold = 1000
user = input("Enter User ")
assert user==expectedUsr

# Acelasi exesrcitiu, varianta mai complicata

userName = input("Enter your username: ")
if len(userName) >= 6 and len(userName) <= 12: # punem un if statement care verifica daca userul are intre 6 si 12 caractere cu ajutorul functiei len
    print("Now enter your password")
    userPassword = input("Enter your password: ")
    if len(userPassword) >= 6 and len(userPassword) <= 12: # daca userul e corect, verificam acelasi lucru si pentru parola
        print("You are able to log in!!!")
    else:
        print("Incorrect password. Choose another.")
else:
    print("Incorrect username. Choose another.")

# Nota: pentru a afla mai multe despre o functie se poate da CTRL+Click pe functia respectiva

# Variabilele sunt case sensitive, si putem sa alocam valoarea de la adresa de memorie a unei variabile la adresa de memorie a altei variabile
# Exemplu
user_5 = 100 #instructiune de definire si initializare a unei variabile
#print(uSer_5) # nu va merge pentru ca numele variabilei este case sensitive, iar sistemul nu va recunoaste numele asta
score = user_5 # atribuirea valorii variabilei user_5 la variabila score
print(score)

# ------------------------------------------------------------------------------------------------------------

""" 2. Input de la tastatura """
x = input("Enter the first number ") # Atribuirea unei valori de la tastatura la o variabila
y = input("Enter second value ")
output = int(x) + int(y) #  conversia fortata (CAST) a unei variabile (by default de la tastatura se defineste string)
output = int(x) % int(y)  # functia modulo - util cand verificam daca un numar este par sau impar - returneaza restul impartirii lui x la y
x,y,z = 1,2,3 # putem sa initializam trei variabile in acelasi timp
print(z)
print(f"{x} with {y} is {output}") # f-ul din fara anunta sistemul ca urmeaza sa trimitem niste valori din niste variabile in interiorul textului de afisat

# ------------------------------------------------------------------------------------------------------------

""" 3. Formatarea in print"""

print(f"{x} with {y} is {output}")  #printarea cu formatare
print(f"{x} modulo {y} is {output}" )

# Alte exemple de formatare:
name = 'Johnny'
age = 55

print('Hi' + name + '. You\'re' + str(age) + 'years old') # Exemplu fara formatare.
                                                             # Am scris You\'re cu caracterul  "\"
                                                                # (numit escape character pentru ca am vrut ca sistemul sa considere
                                                                    # apostroful drept caracter de afisat pe ecran, nu sfarsitul textului)
print(f'Hi {name}, You are {age} years old') # Exemplu cu formatare

# Formatarea inainte de python 3 se facea cu functia .format:
# Exemple:

print('Hi {}. You  are {} years old.'.format('Johnny',55)) # Aici acoladele vor fi inlocuite in ordine cu valorile din paranteze
print('Hi {}. You  are {} years old.'.format(name, age))
print('Hi {new_name}. You  are {new_age} years old.'.format(new_name = 'sally', new_age=100)) # Aici am definit in-line valorile pentru name si age


# ------------------------------------------------------------------------------------------------------------

"""4. CONSTANTE"""

# Constantele nu sunt suportate de python, motiv pentru care orice vrem sa definim ca si constanta
# in python va fi scrisa ca si conventie cu majuscule, pentru a anunta eventualele persoane care vor folosi codul
# Constant = spatiu de memorie care nu isi poate schimba valoarea
# Useful when generating all sort of utilities for automation, where we define test inputs that should not change their behaviour
# Ex: username, sleep between automation test steps (we can agree at project level the sleep time)

PI = 3.14

# ------------------------------------------------------------------------------------------------------------
"""5. Dunder methods -> DUNDER = Double underscore"""

# Exemple de dunders:
_x = 7 #specifica o variabila considerata prin conventie PROTECTED ce nu poate fi folosita in alte pachete. Nu este DUNDER
__x = 8 # Variabilele cu __ sunt considerate prin conventie PRIVATE, dar aceste DUNDER sunt rezervate pentru metode specifice python, si nu este recomandam sa definim variabile de tip DUNDER

#Exemplu de dunders:
if __name__ == '__main__':  # Verifica daca programul este executat individual sau este apelat dintr-un alt program
    print("Another module")
    a: int = 5 # putem sa declaram o variabila si in felul asta specificandu-i in mod explicit tipul de data
    b: str = 'Ana are mere'
    print(type(a))
    print(type(b))
    #c = a + b -> Returneaza eroare de concatenare pentru ca nu putem sa adunam un tip de date numeric cu un tip de date de tip text
    c = str(a) + b
    print(c)
    print(a)

# ------------------------------------------------------------------------------------------------------------

""" 6. Built in functions """

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

# ------------------------------------------------------------------------------------------------------------
""" 7. immutability -> Nu putem sa modificam doar o anumita pozitie intr-o variabila """
selfish = 1
print(selfish)
# selfish[0] = '1212' #Va returna eroare pentru va variabilele sunt immutable

Selfish=[1,45,'test','andrada']
Selfish[0] = '1212' # asta va merge pentru ca selfish nu mai e o variabila ci o lista, si lista nu este immutable
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


    

















