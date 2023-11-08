class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne:
            self.dostupne = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"

    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, Typ vozidla: {self.typ_vozidla}"

# Vytvoření objektů reprezentujících auta 
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)


vyber_znacky = input("Jakou značku si přejete půjčit (Peugeot nebo Škoda)? ").strip()

if vyber_znacky == "Peugeot":
    auto = auto1
elif vyber_znacky == "Škoda":
    auto = auto2
else:
    print("Tuto značku nemáme k dispozici.")


print(auto.get_info())  
print(auto.pujc_auto())  
print(auto.pujc_auto())  # Zkus půjčit znovu (mělo by vrátit, že vozidlo není k dispozici)
