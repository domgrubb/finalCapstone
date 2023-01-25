## Importing modules, changing directory ##
import os
import sys
os.chdir(sys.path[0])

#========The beginning of the class==========
class Shoe:

    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)

    def get_cost(self):
        return self.cost

    def get_quantity(self):
        return self.quantity

    def __str__(self):
        return f'''country: {self.country}
code: {self.code}
product: {self.product}
cost: {self.cost}
quantity: {self.quantity}
'''


#=============Shoe list===========
shoe_list = []

#==========Functions outside the class==============
def read_shoes_data():
    '''First line of file gives order of properties. 
    Properties separated by commas, so split at comma. Shoe object generated using each element of the split list.'''
    try:
        with open("inventory.txt", "r") as f:
            ## Each line represents one shoe, iterating over lines may be helpful to populate list ##
            for count, line in enumerate(f):
                if count > 0:
                    props = line.split(",")
                    ## Assigning each to correct list ##
                    shoe_list.append(Shoe(props[0], props[1], props[2], props[3], props[4]))
        #return shoe_list
    except FileNotFoundError:
        print("File not in current directory, please try again.")
 
def capture_shoes():
    '''Prompts user for properties of the shoe they wish to enter then appends to list of shoes.'''
    ## Prompting user for each individual property ##
    country = input("Please enter the country of origin of the shoe: ")
    code = input("Please enter the code of the shoe: ")
    product = input("Please enter the name of the shoe: ")
    cost = float(input("Please enter the cost of the shoe: "))
    quantity = int(input("Please enter the quantity of pairs of shoes: "))

    ## Creating shoe object, adding to list ##
    new = Shoe(country, code, product, cost, quantity)
    shoe_list.append(new)

def view_all():
    '''Returns every shoe in a string form. To view to console, need to call the function within a "print()"'''
    for shoe in shoe_list: 
        print(shoe.__str__())

def re_stock():
    '''Sorts list of shoes by quantity. Asks user if they wish to restock shoe with lowest remaining quantity
    and if so by how much. Rewrites the inventory file to reflect the new quantity'''

    ## Sorting shoe list, using sorted to generate a separate list ##
    sort_quant = sorted(shoe_list, key = lambda x: x.quantity, reverse = False)
    smallest = sort_quant[0]
    choice = input(f'''The shoe with the lowest remaining quantity is {smallest.product} with {smallest.quantity} remaining.
Do you wish to add to this quantity? Y/N: ''')
    if choice.lower() == "y":
        quant = int(input("Enter how many additional pairs to add: "))
    ## Removing line from file, appending to end with updated quantity ##
    with open("inventory.txt", "r") as f:
        lines = f.readlines()
    with open("inventory.txt", "w") as f:
        for line in lines:
            ## Finding correct line using unique code ##
            if line.split(",")[1] != smallest.code:
                f.write(line)
        f.write(f'''
{smallest.country},{smallest.code},{smallest.product},{smallest.cost},{smallest.quantity + quant}''')
    print("Inventory file updated.")

def search_shoe():
    '''Prompts user for code of shoe they wish to find, then prints the details to the console.'''
    code = input("Please enter the code of the shoe you wish to find: ")
    for shoe in shoe_list:
        if shoe.code == code:
            print(shoe.__str__())
    '''
     This function will search for a shoe from the list
     using the shoe code and return this object so that it will be printed.
    '''

def value_per_item():
    '''Iterates over list of shoes, printing product name and inventory value (cost * quantity).
    After iterating over entire list, prints total value of stock.'''
    tot_value = 0
    for shoe in shoe_list:
        value = shoe.get_cost() * shoe.quantity
        print(f"Value of {shoe.product}: {value}")
        tot_value += value
    print(f"Total value of all shoes: {tot_value}")

def highest_qty():
    '''Sorts list of shoes by quantity, finds shoe with highest quantity and prints product name to console,
    along with putting it on sale.'''
    sort_quant = sorted(shoe_list, key = lambda x: x.quantity, reverse = True)
    highest = sort_quant[0]
    print(f"The shoe with the highest quantity is {highest.product}. This shoe is now on sale!")


#==========Main Menu=============
choice = None
while choice != "e":
    choice = input('''Welcome to the inventory manager, please select an action:
r = read in data from inventory file
a = append inventory with new shoe information
c = view all shoes in current inventory
i = view and increase stock of shoe with least stock remaining
s = search for a shoe by code
v = view value for each product remaining as well as total value
h = view shoe of highest quantity, put on sale
e = exit
''')

    if choice == "r":
        read_shoes_data()

    elif choice == "a":
        capture_shoes()
    
    elif choice == "c":
        view_all()

    elif choice == "i":
        re_stock()
    
    elif choice == "s":
        search_shoe()

    elif choice == "v":
        value_per_item()
    
    elif choice == "h":
        highest_qty()

print("Thank you for using the menu, have a good day!")