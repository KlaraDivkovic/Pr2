"""Napisati rekurzivnu funkciju koja kao parametar prima string,
a kao rezultat taj string ispisuje sa zada."""

def rijecSaZada(a):
    if len(a) !=1:
        return rijecSaZada(a[1::]) + a[0]
    else:
        return a

print(rijecSaZada("Josipa"))
    
