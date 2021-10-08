"""

Calculator class used for operations

-- o functie aflata in interiorul unei clase se numeste metoda
-- un constructor este un bloc de cod care ne poate ajuta sa definim atribute ale clasei valabile in toata clasa
"""

from math import sqrt

from IntroToProgramming.OOP.Curs4 import mathOperations


class Calculator:
    def __init__(self,num1, num2, num3):
        self._num1 = num1 #asta e un atribut al clasei, adica o variabila care apartine clasei
        self._num2 = num2
        self._num3 = num3

    def _max2(self, num1, num2):  # self arata ca metoda este o parte din clasa. Underscore arata prin conventie ca metoda este privata
        if num1 > num2:  # se face comparatia intre cele doua numere
            return num1  # se returneaza num1 daca e mai mare decat num2
        else:
            return num2

    def max3(self, num1, num2, num3):
        return self._max2(num1, self._max2(num2, num3))

    def test_max3(self):
        self.max3(5, 7, 9)

    def max3v2(self):
        a = 2

        def max2v2(num1, num2):
            if num1 > num2:  # se face comparatia intre cele doua numere
                return num1 + a  # se returneaza num1 daca e mai mare decat num2
            else:
                return num2

        return self._max2(self._num1, max2v2(self._num2, self._num3))

    def mathOperations(self, a, b, operation):
        # from IntroToProgramming.OOP.Curs4 import mathOperations -> putem sa importam si local
        return mathOperations(a,b,operation)


# calculator = Calculator()
calculator = Calculator(7,5,11)
print("Rezultatul este",calculator)
print("Rezultatul functiei test_max3() este: ", calculator.test_max3())  # returneaza none pentru ca metoda nu are return
print("Rezultatul functiei max3() este: ", calculator.max3(5,6,7))
print("Rezultatul functiei mathOperations este:  ",calculator.mathOperations(2,4,"*"))
print(calculator.max3v2())
