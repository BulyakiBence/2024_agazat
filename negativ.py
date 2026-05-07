import random
def negativ(szam):
    if szam > 0:
        return True
    else:
        return False
negativak = []
for i in range (100):
    szam = random.randint(-50,50)
    if negativ(szam):
        negativak.append(szam)
print(f"Ennyi negatív számot kaptál: {len(negativak)}")