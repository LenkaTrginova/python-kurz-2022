#1.Zadání
jmeno = input('Zadej jmeno')
print(jmeno + '@czechitas.cz')

#2.Bonus 
jmeno_a_prijmeni=input('Zadej jmeno a prijmeni')
#a) 
print(jmeno_a_prijmeni.upper())
#b)
print(jmeno_a_prijmeni.lower())
#c)
print(jmeno_a_prijmeni.title())
#d) 
jmeno_a_prijmeni_split=jmeno_a_prijmeni.split(' ')
print((jmeno_a_prijmeni_split[0][0] + jmeno_a_prijmeni_split[1][0]).upper())
#e)
if len(jmeno_a_prijmeni_split[0]) > 5:
    print(jmeno_a_prijmeni_split[0][0].title() + (jmeno_a_prijmeni_split[1].title()))
else: 
    print(jmeno_a_prijmeni_split[0].title() + jmeno_a_prijmeni_split[1].title())
