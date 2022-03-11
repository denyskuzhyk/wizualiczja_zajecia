#zadanie 9
import math

liczba = int(input("podaj liczbe "))
try:
    result = math.sqrt(liczba)
    print(result)

except ValueError:
    print("podana wartosc ujemna")