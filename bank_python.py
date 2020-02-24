print("start")
print("mögliche Operationen:")
print("einzahlung / auszahlung / kontostand")
credit = 10.00

while True:

    operation=str(input("operation eingeben:"))

    if (operation == "einzahlung") or (operation == "Einzahlung"):
        deposit=float(input("Bitte geben sie einen Betrag zum Einzahlen ein:"))
        credit += deposit
        print(f"ihr neuer Kontostand beträgt: {credit}€")
        print()

    elif (operation == "auszahlung") or (operation == "Auszahlung"):
        disbursment=float(input("Bitte geben sie einen Betrag zur Auszahlung an:"))
        if (credit - disbursment) < 0:
            print("ihr Guthaben reicht nicht aus")
        elif (credit - disbursment) >= 0:
            credit -= disbursment
            print(f"ihr neuer Kontostand beträgt: {credit}€")
            print()

    elif (operation == "kontostand") or (operation == "Kontostand"):
        print(f"ihr Kontostand beträgt: {credit}€")
        print()