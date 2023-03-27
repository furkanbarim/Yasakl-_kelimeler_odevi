yasakli_liste = ["Furkan", "Tutku", "Mustafa", "Sümeyye"]

metin: str = input("Lütfen Metin giriniz: ")

for i in yasakli_liste:
    if i in metin:
        metin = metin.replace(i, len(i)*"*")
print(metin)