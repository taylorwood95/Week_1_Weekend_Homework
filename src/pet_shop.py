# WRITE YOUR FUNCTIONS HERE


def get_pet_shop_name(pet_shop):
    return pet_shop["name"]


def get_total_cash(pet_shop):
    return pet_shop["admin"]["total_cash"]


def add_or_remove_cash(pet_shop, amount):
    pet_shop["admin"]["total_cash"] += amount


def add_or_remove_cash_remove(pet_shop, amount):
    pet_shop["admin"]["total_cash"] -= amount


def get_pets_sold(pet_shop):
    return pet_shop["admin"]["pets_sold"]


def increase_pets_sold(pet_shop, amount):
    pet_shop["admin"]["pets_sold"] += amount


def get_stock_count(pet_shop):
    return len(pet_shop["pets"])


def get_pets_by_breed(pet_shop, breed):
    total_breed = []
    index = 0
    for pet in pet_shop:
        if pet_shop["pets"][index]["breed"] == breed:
            total_breed.append(pet)
            index += 1
    return total_breed


def get_pets_by_breed_not_found(pet_shop, breed):
    total_breed = []
    index = 0
    for pet in pet_shop:
        if pet_shop["pets"][index]["breed"] == breed:
            total_breed.append(pet)
            index += 1
    return len(total_breed)


def find_pet_by_name(pet_shop, name):
    for pets in pet_shop["pets"]:
        if pets["name"] == name:
            return pets


def remove_pet_by_name(pet_shop, name):
    for pets in pet_shop["pets"]:
        if pets["name"] == name:
            pet_shop["pets"].remove(pets)


def add_pet_to_stock(pet_shop, new_pet):
    pet_shop["pets"].append(new_pet)


def get_customer_cash(customers):
    return customers["cash"]


def remove_customer_cash(customer, amount):
    customer["cash"] -= amount


def get_customer_pet_count(customer):
    return len(customer["pets"])


def add_pet_to_customer(customer, new_pet):
    customer["pets"].append(new_pet)


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False


def customer_can_afford_pet(customer, new_pet):
    if customer["cash"] >= new_pet["price"]:
        return True
    return False


def sell_pet_to_customer(pet_shop, pet, customer):
    if pet in pet_shop["pets"] and customer["cash"] >= pet["price"]:
        customer["pets"].append(pet)
        pet_shop["admin"]["pets_sold"] += 1
        customer["cash"] -= pet["price"]
        pet_shop["admin"]["total_cash"] += pet["price"]


# def sell_pet_to_customer(pet_shop, pet, customer):
#     if pet != None and customer_can_afford_pet(customer, pet):
#         remove_pet_by_name(pet_shop, pet["name"])
#         add_pet_to_customer(customer, pet)
#         remove_customer_cash(customer, pet["price"])
#         add_or_remove_cash(pet_shop, pet["price"])
#         increase_pets_sold(pet_shop, 1)
