"""Koristeći listu imena iz prethodnog zadatka svakom studentu generirati nasumičnu ocjenu od 1 do 5.
Prebrojati u rječnik koliko ima kojih ocjena.
Izračunati postotak prolaznosti. (sve ocjene veće od 1)."""

import random

imena = ['Josip', 'Ivan', 'Ivan', 'Josip', 'Ivan', 'Ivan', 'Katarina', 'Božena', 'Ivona', 'Marija', 'Josipa', 'Marko', 'Dario', 'Mihael',
'Stana', 'Bruno', 'Anamarija', 'Andrea', 'Petar', 'Marko', 'Amnesa', 'Nikola', 'Antonela', 'Leon', 'Ivan', 'Ante', 'Ivan',
'Jure', 'Jan', 'Florijan', 'Boris', 'Ivan', 'Stipe', 'Damir', 'Ana', 'Tin', 'Iva', 'Kristina', 'Josip', 'Tomislav', 'Luka', 'Ivan',
'Martin', 'Marko', 'Ante', 'Nikolina', 'Ivan', 'Toni', 'Ante', 'Darija', 'Dominik', 'Lucija', 'Luka', 'Ana', 'Emanuel',
'Petar', 'Matej', 'Stjepan', 'Josip', 'Luka', 'Marija', 'Toni', 'Iva ', 'Perica', 'Antonio', 'Ante', 'Marijan', 'Mario',
'Antonio', 'Stipe', 'Filip', 'Ivan', 'Ivan', 'Luka', 'Ante Bruno', 'Ivan', 'Vinko', 'Ivan', 'Matijas', 'Ivan', 'Freda', 'Kristina',
'Josip', 'Lucija']


ukupno_studenata = len(imena)

#print(ukupno_studenata)

studenti= dict()

for ime in imena:
    studenti[ime] = 0

for ime in imena:
    if ime in studenti:
        studenti[ime] += 1
    else:
        studenti[ime] = 1

#print(studenti)

pojedinacna_imena = []
kljuc = studenti.keys()
for ime in kljuc:
    pojedinacna_imena.append(ime)

ocjene = dict()
pozitivne = 0
nedovoljan = 0
dovoljan = 0
dobar = 0
vrlo_dobar = 0
odlican = 0

for ime in pojedinacna_imena:
    for i in range (studenti[ime]):
        ocjene[ime + str(i+1)] = random.randint(1, 5)
        if ocjene [ime + str(i+1)] > 1:
            pozitivne += 1
        if ocjene [ime + str(i+1)] == 1:
            nedovoljan += 1
        if ocjene [ime + str(i+1)] == 2:
            dovoljan += 1
        if ocjene [ime + str(i+1)] == 3:
            dobar += 1
        if ocjene [ime + str(i+1)] == 4:
            vrlo_dobar += 1
        if ocjene [ime + str(i+1)] == 5:
            odlican += 1

ocjena_studenta= ocjene.items()
for ime, ocjena in ocjena_studenta:
    print(ime, ":", ocjena)

prosjek = (pozitivne / ukupno_studenata)*100
print("Postotak prolaznosti je:", prosjek, "%")
print("Nedovoljnih je:", nedovoljan)
print("Dovoljnih je:", dovoljan)
print("Dobrih je:", dobar)
print("Vrlo dobrih je:", vrlo_dobar)
print("Odličnih je:", odlican)





