# Purpose: Defines an item class that stores information on price.
# Author: Michael Lee (mzl28)
# Date: April 14, 2023

class Item:
    def __init__(self, name, price, taxable):
        self.__name = name
        self.__price = price
        self.__taxable = taxable
        
    def itemToString(self):
        itemName = self.__name.ljust(32, '_')
        itemPrice = "{:.2f}".format(self.__price).rjust(8, '_')
        return itemName + itemPrice

    def getPrice(self):
            return self.__price
        
    def getTax(self, taxRate=0.07):
        if self.__taxable:
            return self.__price * taxRate
        else: 
             return 0.0
        
