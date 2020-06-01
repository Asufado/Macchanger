#! /usr/bin/python3
# -*- coding: utf-8 -*-

from os import system



#Holt sich den Input des Users.
wlan = input("Wireless Karte die benützt werden soll: ")
wahl = input("Möchtest du eine zufällige MAC-Adresse(Y/N)? ")



#Setzt die zufällige MAC-Adresse
if wahl == "Y":

    # Setzt den String für die zufällige MAC fest.
    zufällig = "ifconfig {0} down && macchanger -r {0} && ifconfig {0} up".format(wlan)
    for i in range(0,50):
        system(zufällig)

    for i in range(0,100):
        print(" ")

    print("Deine MAC-Adresse wurde erfolgreich geändert!")


#Setzt die bestimmte MAC-Adresse
elif wahl == "N":

    mac = input("Wunsch Mac-Addresse: ")
    # Setzt den String für die bestimmte MAC fest.
    bestimmt = "ifconfig {0} down && macchanger --mac {1} {0} && ifconfig {0} up".format(wlan, mac)

    for i in range(0, 50):
        system(bestimmt)

    for i in range(0, 100):
        print(" ")

    print("Deine MAC-Adresse wurde erfolgreich geändert!")


else:
    for i in range(0,100):
        print(" ")

    print("Achte auf die Groß-/Kleinschreibung! Versuch es erneut!")