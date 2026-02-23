def discount(price, isPet, nItems):
    risultato = 0.0
    base_sconto = 0.0
    numero_animali = 0
    if len(set(isPet)) == 2:
        index = 0 
        for i in isPet:
            if i:
                numero_animali += 1
            else:
                base_sconto += price[index]
            index += 1
        if (nItems - numero_animali) >= 5:
            risultato = base_sconto + 0.2
    return risultato

def main():
    prices = []
    isPet = []
    sconto = 0.0
    with open("lista.txt", "r") as f:
        lines = f.readlines()
        for line in lines:
            parts = line.split()
            prices.append(float(parts[0]))
            if parts[1].upper() == "Y":
                isPet.append(True)
            else:
                isPet.append(False)


    nItems = len(prices)
    if nItems == len(isPet):
        sconto = discount(prices, isPet, nItems)
        print(f"{sconto:.2f}")

if __name__ == "__main__":
    main()