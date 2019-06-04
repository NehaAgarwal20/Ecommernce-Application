'''#group1 Electronic Commerce Application. 
You need to create the foundations of an e-commerce engine
for a B2C (business-to-consumer) retailer. You need to have a class for a customer
called User, a class for items in inventory called Item, and a shopping cart class called
Cart. Items go in Carts, and Users can have multiple Carts. Also, multiple items can
go into Carts, including more than one of any single item.

#'''

class User:
    def __init__ (self, userName, userAddress, paymentMethod):
        self.userName = userName
        self.userAddress = userAddress
        self.paymethod = paymentMethod
    def addUser (self, userName):
        self.userName = userName

class Carts:
    def __init__ (self, numItems, itemName, itemQuantity):
        self.numItems = numItems
        self.itemName = itemName
        self.itemQuant = itemQuantity
    def addToCart():
        userinput_item = int(input('\n Enter the index of the product you want: '))
        carts.append(items_dict[userinput_item])
    def printcart():
        carts_1 = set(carts)
        print("\n \n")
        for i in carts_1:
            print(f'{i} : {carts.count(i)}')
        print(" \n Total Number of Items:" , len(carts))

class Item:
    def printInventory():
            print ("\n Inventory Available: \n",  *items_dict.items(), sep = '\n')

uName = input("Enter Username: ")
uAddress = input("Enter your address: ")
uPayMethod = input("Payment Method: Cash/Card? ")
FirstUser = User(uName,uAddress,uPayMethod)
items = ['3M Tape', 'iPhone X', 'Macbook Air', 'Milton Medical Box', 'Measuring Tape', 'DeWalt Drill Machine', 'Casio Watch', 'Kleenex Paper Towel', 'Microfibre Towel', 'Samsung Vacuum Cleaner']
items_dict = {}
for i, item in enumerate(items):
    items_dict.update( {i : item} )
carts = []
Item.printInventory()
Carts.addToCart()
while input("\n \n Do you want to add another item? ") in ['Y', 'y', 'Yes', 'yes']:
    Item.printInventory()
    Carts.addToCart()
Carts.printcart()
print("Username:" , uName)
print("Your Address:" , uAddress)
print("Your Payment Method:", uPayMethod)
