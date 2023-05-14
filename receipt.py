# Purpose: Creates a receipt for the customer at the end of transaction
# Author: Michael Lee (mzl28)
# Date: April 14, 2023


class Receipt:
    def __init__(self, tax_rate = 0.07):
        self.__tax_rate = tax_rate
        self.__purchases = []

    def receiptToString(self):
        receiptString = "----- Receipt time -----\n"
        #receiptString = "----- Receipt {} -----\n".format(str(datetime.datetime.now())
        total = 0.0
        tax= 0.0

        for item in self.__purchases: 
            receiptString += item.itemToString() + "\n"
            tax += item.getTax()
            total += item.getPrice()


    
        receiptString += "{:<16}{:>4.2f}\n".format("\nSub Total___________________________", total)
        receiptString += "{:<16}{:>4.2f}\n".format("Tax_________________________________", tax)
        receiptString += "{:<16}{:>4.2f}\n".format("Total_______________________________", total+tax)

        return receiptString
    

    def addItem(self, item):
        self.__purchases.append(item)

