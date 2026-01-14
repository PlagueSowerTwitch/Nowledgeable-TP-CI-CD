a = 2 
print("coucou", a)

def moyenne(liste):
    return sum(liste) / len(liste)

print(moyenne([1,2,3,4,5,6,7,8,9]))

def moyenne_erreur(liste):
    return sum(liste) / len(liste) + 1 # Bug Volontaire

print(moyenne_erreur([1,2,3,4,5,6,7,8,9]))