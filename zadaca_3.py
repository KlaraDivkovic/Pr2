import re
#Potrebno napisati regex koji vraca podudaranje ukoliko se unese string koji
#počinje kao prvo slovo vašeg imena, a završava kao prvo slovo
#prezimena. String mora sadržavati bar jedan broj između 0 i 5 i razmak.
while 1:
    rijec=input("Unesite rijec:")
    regex="^K.*[0-5].*\s.*Ć$"
    result=re.findall(regex, rijec)
    print(result)
    if result:
        print("dobar unos")
        break
    else:
        print("pogresan unos")
    
