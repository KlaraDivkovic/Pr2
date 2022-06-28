"""Napisati regex za provjeru validnosti unosa e-maila.
E-Mail mora biti formata ime.prezime@fpmoz.sum.ba Nakon toga napisati regex
za provjeru eduId koji mora biti formata iprezimeX@sum.ba gdje je i prvo slovo
imena + prezime. X predstavlja bilo koji broj (moze ici u beskonacnost),
a taj broj ne mora postojati (može biti samo iprezime@sum.ba).
Od korisnika zatražiti unos maila i eduid te ispisati uspješnost.
Istražiti greedy i non-greedy quantifiers."""


import re

regex1 = "^[a-z]\.[a-z]@fpmoz.sum.ba$"
regex2 = "^[a-z]([0-9]*)@sum.ba$"

while 1:
    email = input("Umesite email:")
    eduid = input("Unesite EduId:")
    rezultat1 = re.search(regex1, email)
    rezultat2 = re.search(regex2, eduid)
    if rezultat1 and rezultat2:
        print("Unijeli ste ispravan unos!")
        break
    else:
        print("Unijeli ste pogresan unos!")
