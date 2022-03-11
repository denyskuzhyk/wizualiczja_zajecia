#zadanie 6
lista = []
liczba1 = input("podaj liczbe ")
max = liczba1

for i in range(2):
    liczba = input("podaj liczbe ")
    if liczba > max:
        max = liczba

print(f"najwieksza liczba to {max}")