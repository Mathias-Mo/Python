from function import *


def init():

    # 6 Lottozahlen erstellen
    ziehung = random_numbers(6, 49)
    # userzahlen erzeugen
    # userzahlen = [1, 2, 3, 4, 5, 6]
    userzahlen = user_numbers(6)
    # ziehung = [7, 8, 9, 10, 11, 12]
    # Lottozahlen anzeigen
    print("Ziehung: ", numberListShow(ziehung))
    # userzahlen anzeigen
    print("Deine Zahlen: ", numberListShow(userzahlen))
    # Die Listen vergleichen und treffer anzeigen
    treffer = lotozahl_finden(ziehung, userzahlen)
    print("Du hast " + str(treffer) + " Treffer")


if __name__ == "__main__":
    init()
