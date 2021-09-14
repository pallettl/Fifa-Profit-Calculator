#Import Modules
import time

#Check if the file for writing previous sales exists on the system, and if not create one
f = open("playerSalesList", "w")
f.close()

#Ask the user the player's name and rarity so it can be written to a file
playerName = str(input("playerName? "))
playerRarity = str(input("playerRarity? "))

#Ask the user the price they bought and sold the card for
boughtPrice = float(input("boughtPrice? "))
sellPrice = float(input("sellPrice? "))

#Calculate the profit after tax
priceAfterTax = sellPrice * 0.95
profit = priceAfterTax - boughtPrice

#Tell the user the profit they made and how much the card sold for in the end
print("\n" + playerName + " " + playerRarity)
time.sleep(1)
print("Card sold for " + str(priceAfterTax) + " coins.")
time.sleep(1)
print("Profit of " + str(profit) + " coins.")

#Add all variables to a list so it can be written to a file
playerList = [playerName, playerRarity, boughtPrice, sellPrice, priceAfterTax, profit]

#Write to the file
f = open("playerSalesList", "w")
f.write(str(playerList))
f.write("\n")
f.close()