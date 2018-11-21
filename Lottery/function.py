import random


# count zufällige Zahlen erzeugen
def random_numbers(count, out_number):
    i = 1
    lottozahlen = []
    ziehung = []
    # liste von 1 bis von_number + 1 erzeugen
    for x in range(1, out_number + 1):
        lottozahlen.append(x)
    random.shuffle(lottozahlen)  # liste mischen
    # die ersten count Zahlen in die Liste ziehung eintragen
    for idx, lottozahl in enumerate(lottozahlen):
        if idx < count:
            ziehung.append(lottozahl)
    return ziehung              # Die Ziehung ausgeben


def user_numbers(count):
    userzahlen = []

    for x in range(1, count + 1):
        userzahl = input("Bitte die " + str(x) + ". Zahl eingeben")
        userzahl = int(userzahl)
        userzahlen.append(userzahl)
    return userzahlen


def lotozahl_finden(ziehung, userzahlen):
    treffer = 0
    for lottozahl in ziehung:
        if lottozahl in userzahlen:
            treffer += 1
    return treffer


def numberListShow(liste):
    return " ".join(map(str, liste))

