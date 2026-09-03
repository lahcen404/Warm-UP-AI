## Challenge 1




#  Écrivez du code Python ici

liste1 = [1, 3, 5, 3]
liste2 = [2, 3, 4, 5]

liste1.extend(liste2)

sans_double = set(liste1)

sorteed = sorted(sans_double)

print(sorteed)