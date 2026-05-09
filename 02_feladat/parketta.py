szelesseg = float(input("Adja meg a szoba szélességét méterben: "))
hossz = float(input("Adja meg a szoba hosszat meterben: "))
csomag = int(input("Hány csomag parkettánk van: "))

terulet = szelesseg*hossz
print(f"A szoba terulete {terulet} negyzetmeter")
kell_hozza = csomag * 2
if kell_hozza < terulet:
    print("Kell hozzá még parketta!")
else:
    print("VAn elég parketta.")
