class Menu:
    def __init__(self):
        self.categories = []
        self.menu_list = []
        self.bought_product_list = []

    def open_menu(self):
        with open("menu.txt") as menu_file:
            all_items = menu_file.readlines()  #returns list of all lines
            for n_item in range(1, len(all_items)): #selects items from menu and add each of them to the list of menu
                menu_item = all_items[n_item] 
                new_item = menu_item.split(";")
                for item in range(len(new_item)):
                    new_item[item] = new_item[item].strip()  
                item_object = Menu()
                item_object.category = new_item[0]
                item_object.name = new_item[1]
                item_object.portion = new_item[2]
                item_object.price = new_item[3]
                self.menu_list.append(item_object)  

    def get_categories(self):  #gets categories in the menu.txt and adds them to list called categories.
        categories = []
        for i in self.menu_list:
            if i.category not in categories:
                categories.append(i.category)
        self.categories = categories

    def get_category_names(self, category):  #get rids of the repeated items in the list category 
        category_names = []                  #then adds them to the list called category names
        for i in self.menu_list:
            if (i.category == category) and i.name not in category_names:
                category_names.append(i.name)
        self.category_names=category_names
        return category_names

    def get_portions(self, name):  #gets portions from the menu_list and adds them to portions list
        portions = []
        for i in self.menu_list:
            if i.name == name:
                portions.append(i.portion)
        self.portions = portions
        return portions

    def categories(self): #displays a list of categories.
        print("Product Categories")
        count = 1
        for i in self.categories:
            print(f"{count}. {i}")
            count += 1
    
    def get_order(self):

        Menu.categories(self)   #selects the product category
        choice_of_category = int(input("Please select product category: "))
        while choice_of_category > len(self.categories) or choice_of_category <= 0: # input validity check
            choice_of_category = int(input("Please select product category: "))
        choice_of_category = self.categories[ choice_of_category -1]
        print("-"*59)

        names = Menu.get_category_names(self, choice_of_category)   #selects the product name.
        list_names(choice_of_category, names)
        choice_of_name = int(input("Please select product name: "))
        while choice_of_name > len(self.category_names) or choice_of_name <=0: # input validity check
            choice_of_name = int(input("Please select product name: "))
        choice_of_name = self.category_names[choice_of_name-1]
        print("-"*59)

        portions = Menu.get_portions(self, choice_of_name)    #selects the product portion.
        list_portions(choice_of_name, portions)
        choice_of_portion = int(input("Please select product portion: "))
        while choice_of_portion > len(self.portions) or choice_of_portion <= 0: # input validity check
            choice_of_portion = int(input("Please select product portion: "))
        choice_of_portion = self.portions[choice_of_portion-1]
        print("-"*59)
  
        for i in self.menu_list:    #save the selected product to the list.
            if (i.category == choice_of_category) and (i.name == choice_of_name) and (i.portion == choice_of_portion):
                self.bought_product_list.append([i.name, i.portion, i.price])
        print("1. Add New\n"
              "2. Checkout")
        user_choice = int(input("Please select an operation:"))
        while not((user_choice == 1) or (user_choice == 2)):  #Input check.
            user_choice = int(input("Invalid Input\n"
                                    "Please select an operation:"))
        if user_choice == 1:
            Menu.get_order(self) 
        elif user_choice == 2:
            display_receipt(self.bought_product_list)
            total = 0
            for i in self.bought_product_list:
                total += float(i[2].replace("$",""))
            total = format(total,".2f")
            print("Total:{:>53}".format("$"+str(total)))

# The function bellow, list_names, adds products' names into a list(names)
def list_names(category, names):
    print(f"Products in {category}:")
    count = 1
    for i in names:
        print(f"{count}. {i}")
        count += 1

# The function bellow, list_portions, adds portions into a list(portions)
def list_portions(name, portions):
    print(f"{name} Portions:")
    count = 1
    for i in portions:
        print(f"{count}. {i}")
        count += 1

# The function bellow, display_receipt, gives a reciept for the bill  
def display_receipt(list_of_items):
    print("-"*59)
    for item in list_of_items:
        print(f"{item[0]: <32} {item[1]: ^20} {item[2]: >5}")
    print("-"*59)

def main():
    menu = Menu()
    menu.open_menu()  
    menu.get_categories()  
    menu.get_order()
main()
