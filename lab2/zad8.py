#zadanie 8
lista = []
count = 1

while(count <= 10):
    liczba = int(input("podaj liczbe "))
    if liczba % 2 == 0:
        lista.append(liczba)

    count += 1

print(lista)