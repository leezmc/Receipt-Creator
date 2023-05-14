# Purpose: Initiates user interaction so that they can enter their items and prices.
# Author: Michael Lee (mzl28)
# Date: April 14, 2023

from item import Item
from receipt import Receipt
import datetime


def main():
	print("Welcome to Receipt Creator")
	receipt = Receipt()

	while True:
		name = input("Enter Item name: ")
		price = float(input("Enter Item Price: "))
		taxable = input("Is the item taxable (yes/no): ")
		

		item = Item(name, price, taxable)
		receipt.addItem(item)

		if input("Add another item (yes/no): ") == 'no':
			break
	print(Receipt.receiptToString(receipt))


if __name__=="__main__":
	main()


