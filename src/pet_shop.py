def get_pet_shop_name(pet_shop):
    return pet_shop["name"]

def get_total_cash(pet_shop):
    money = pet_shop["admin"]["total_cash"]
    return money

def add_or_remove_cash(pet_shop, cash):
    #take the original cash total and adds cash 
    pet_shop["admin"]["total_cash"] += cash

def get_pets_sold(pet_shop):
    current_total = pet_shop["admin"]["pets_sold"]
    return current_total

def increase_pets_sold(pet_shop, sales):    
    pet_shop["admin"]["pets_sold"] += sales

def get_stock_count(pet_shop):
    return len(pet_shop["pets"])

def get_pets_by_breed(pet_shop, breed):
    given_breed = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed:
            given_breed.append(pet)
    return given_breed

def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return pet
        elif pet == None: 
            return 

def remove_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            pet_shop["pets"].remove(pet)

def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)

def get_customer_cash(customers):
        return customers["cash"]

def remove_customer_cash(customers, cash):
    customers["cash"] -= cash

def get_customer_pet_count(customers):
    return len(customers["pets"])

def add_pet_to_customer(customers, new_pet):
    customers["pets"].append(new_pet)

# def customer_can_afford_pet(customer, can_buy_pet):
#     if customer["cash"] >= ["pets"]["price"]:
#         return can_buy_pet == True
#     elif customer["cash"] <= ["pets"]["price"]:
#         return == False
