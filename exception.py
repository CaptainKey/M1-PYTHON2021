


a = [1,2,3,4,5]
taille = len(a)
print(taille)

try:
    a[taille]
except IndexError:
    print("Probleme indice")

if a[0] != 2:
    raise TypeError("Mauvaise valeur")