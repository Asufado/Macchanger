#! /usr/bin/python3
# -*- coding: utf-8 -*-

from os import system



#Gets the user's input.
wlan = input("Which wireless card should be used?: ")
choice = input("Do you want a random MAC address?(Y/N) ")



#Sets the random MAC-Address
if choice == "Y":

    random = "ifconfig {0} down && macchanger -r {0} && ifconfig {0} up".format(wlan)
    for i in range(0,50):
        system(random)

    for i in range(0,100):
        print(" ")

    print("Your MAC-Address has been changed!")


#Sets the specific MAC-Address
elif choice == "N":

    mac = input("MAC-Address you want to have: ")
    # Setzt den String für die bestimmte MAC fest.
    specific = "ifconfig {0} down && macchanger --mac {1} {0} && ifconfig {0} up".format(wlan, mac)

    for i in range(0, 50):
        system(specific)

    for i in range(0, 100):
        print(" ")

    print("Your MAC-Address has been changed!")


else:
    for i in range(0,100):
        print(" ")

    print("Please write the Y/N in upper letters!")