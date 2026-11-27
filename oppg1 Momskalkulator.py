# Oppg1 Momskalkulator ISAK


# Definerer funksjonen "med_moms"
def med_moms(pris, momsprosent):
    totalpris = pris * (1 + momsprosent / 100)
    return round(totalpris,1)
def uten_moms(pris, momsprosent):
    totalpris = pris * (1 - momsprosent / 100)
    return round(totalpris,1)

varepris = []
momsliste = []
inkl_moms = []
# Ber brukeren om å skrive inn en pris og om det skal beregnes med moms, samt momsprosenten.
while True:

    pris = float(input("Hvor mye koster varen? Skal du ikke kjøpe noe, skriver du 0: "))
    if pris == 0:
        break
    momsprosent = float(input("skal det beregnes med moms? Skriv inn momsprosenten 0, 12, 15 eller 25: "))
    moms_med = input("1 hvis pris er inkludert moms")
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
#   print(varepris[i])
#   print(momsliste[i])

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
if moms_12 > 0: print(f"Hvor mange kroner du betalte på 12% momssatts: {moms_12}kr")
if moms_15 > 0: print(f"Hvor mange kroner du betalte på 15% momssatts: {moms_15}kr")
if moms_25 > 0: print(f"Hvor mange kroner du betalte på 25% momssatts: {moms_25}kr")
   
    
