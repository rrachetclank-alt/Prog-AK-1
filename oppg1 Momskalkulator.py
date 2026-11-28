# Oppg1 Momskalkulator ISAK

# her definerer funksjonene for å beregne pris med og uten moms
def med_moms(pris, momsprosent):
    totalpris = pris * (1 + momsprosent / 100)
    return round(totalpris,1)
def uten_moms(pris, momsprosent):
    totalpris = pris * (1 - momsprosent / 100)
    return round(totalpris,1)
# lister for å lagre pris, momsprosent og om det er inkludert moms eller ikke
varepris = []
momsliste = []
inkl_moms = []
# Ber brukeren om å skrive inn en pris og om det skal beregnes med moms og momsprosenten.
# Informasjons-samleren!
dekorasjon = "¨" * 60
dekorasjon2 = "¤" * 60

print(dekorasjon)
print("Velkommen til momskalkulatoren!") 
while True:
    print(dekorasjon)
    pris = float(input("Skal du ikke kjøpe noe eller er ferdig skriver du 0\nHvor mye koster varendu skal kjøpe?\nBeløp: "))
    if pris == 0:
        break
    print(dekorasjon)
    momsprosent = float(input("skal det beregnes med moms? \nSkriv inn momsprosentene 0, 12, 15 eller 25: "))
    print(dekorasjon)
    moms_med = input("Skriv 1 hvis der er inkludert moms og 0 hvis det er uten: ")
    if moms_med == "1":
        inkl_moms.append(1) 
        
    else: 
        inkl_moms.append(0)
    varepris.append(pris)
    momsliste.append(momsprosent)

total = 0
moms_12 = 0
moms_15 = 0
moms_25 = 0

for i in range(len(varepris)):

    if inkl_moms[i] == 1:
        total_u_moms = uten_moms(varepris[i], momsliste[i])
        total_m_moms = varepris[i]
    else:    
        total_m_moms = med_moms(varepris[i], momsliste[i])
        total_u_moms = varepris[i]
    
    print(f"Totalpris med moms: {total_m_moms}kr")
    print(f"Totalpris uten moms: {total_u_moms}kr")
    print(f"samlet moms kostnad: ", (total_m_moms-total_u_moms))

    total += total_m_moms
    if momsliste[i] == 12:
        moms_12 += total_m_moms - total_u_moms
    elif momsliste[i] == 15:
        moms_15 += total_m_moms - total_u_moms
    elif momsliste[i] == 25:
            moms_25 += total_m_moms - total_u_moms

print(f"Totalsummen ble: {total}kr")
if moms_12 > 0: print(f"Hvor mange kroner du betalte tilsammen på 12% momssatts: {moms_12}kr")
if moms_15 > 0: print(f"Hvor mange kroner du betalte tilsammen på 15% momssatts: {moms_15}kr")
if moms_25 > 0: print(f"Hvor mange kroner du betalte tilsammen på 25% momssatts: {moms_25}kr")
   
    
