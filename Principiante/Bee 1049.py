palabra_1 = input()
palabra_2 = input()
palabra_3 = input()
animal = ''
if palabra_1 == 'vertebrado':
        if palabra_2 == 'ave':
                if palabra_3 == 'carnivoro':
                        animal = 'aguia'
                elif palabra_3 == 'onivoro':
                        animal = 'pomba'
        elif palabra_2 == 'mamifero':
                if palabra_3 == 'onivoro':
                        animal = 'homem'
                elif palabra_3 == 'herviboro':
                        animal = 'vaca'
elif palabra_1 == 'invertebrado':
        if palabra_2 == 'inseto':
                if palabra_3 == 'hematofago':
                        animal = 'pulga'
                elif palabra_3 == 'herbivoro':
                        animal = 'lagarta'
        elif palabra_2 == 'anelideo':
                if palabra_3 == 'hematofago':
                        animal = 'sanguessuga'
                elif palabra_3 == 'onivoro':
                        animal = 'minhoca'
print(animal)

