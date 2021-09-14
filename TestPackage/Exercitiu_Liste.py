# Definire Liste
a = [1,2,3] #Listele sunt definite intotdeauna intre paranteze drepte
b = ['banane','mere','gutui']
c = [4, 'struguri',True]

print(a)
print(b)
print(c)
print(a,b,c)
# Fiecare element dintr-o lista se afla la o anumita pozitie. In orice lista, prima pozitie este plasata la indicele 0
print(a[0])
print(b[0])
print(c[0])
print(a[0],b[0],c[0])
print("Ultimul caracter din fiecare lista e: ", a[-1], b[-1],c[-1])  #Afiseaza ultimul caracter
print("Ultimul caracter din fiecare lista e: ", a[2],b[2],c[2])  #Afiseaza ultimul caracter
# print(a[3])  #Returneaza eroare: IndexError: list index out of range. In cazul asta executarea restului de instructiuni se va opri
                                                                        #Acelasi lucru cand se vor executa testele automate
print("Primele doua elemente din lista a sunt:", a[0:2])  #Afiseaza primele doua elemente din lista
print("Elementele din lista a sunt:", a[0:3])  #Afiseaza toate elementele din lista. Nu da eroare daca specifici un numar mai mare
print("Elementele din lista a sunt:", a[0:len(a)])  #Afiseaza toate elementele din lista.
                                                    # len este prescurtarea de la length si arata cate elemente sunt in lista respectiva
print(b.count("mere")) #Functia count arata cate  elementele din cele mentionate in paranteza exista in lista respectiva
c[-1] = "Portocale" #Modifica un singur element din lista

print(sum(a)) #Calculeaza suma tuturor elementelor din lista a

a.clear()
print(a)

a.append("banane")
print(a)
a.append("3")
print(a)