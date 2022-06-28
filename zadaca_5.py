"""Napraviti generator funkcije za ispis svih parnih i svih neparnih brojeva
manjih od prosljeđenog parametra."""

def parni(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

def neparni(n):
    for i in range(n):
        if i % 2 != 0:
            yield i


a = int(input("Unesite neki broj:"))
generator_parnih = parni(a)
generator_neparnih = neparni(a)

brojevi = zip(generator_parnih, generator_neparnih)

for parni_br, neparni_br in brojevi:
    print("Parni:", parni_br, "Neparni:", neparni_br)
