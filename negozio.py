def discount(prices, isPet, nItems):
    numero_animali = sum(isPet)
    numero_altri = nItems - numero_animali

    if numero_animali >= 1 and numero_altri >= 5:
        totale_altri = sum(prices[i] for i in range(nItems) if not isPet[i])
        return totale_altri * 0.20

    return 0.0

def main():
    prices = []
    isPet = []
    with open("lista.txt", "r", encoding="utf-8") as f:
        for line in f:
            clean = line.strip()

            if not clean or clean.startswith("#"):
                continue

            parts = clean.split()
            if len(parts) < 2:
                continue

            try:
                prices.append(float(parts[0]))
            except ValueError:
                continue

            isPet.append(parts[1].upper() == "Y")

    nItems = len(prices)
    if nItems == 0:
        print("0.00")
        return

    sconto = discount(prices, isPet, nItems)
    print(f"{sconto:.2f}")


if __name__ == "__main__":
    main()