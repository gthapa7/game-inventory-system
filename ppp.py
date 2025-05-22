inventory = [
    {"name": "Sword", "category": "Weapon", "value": 100, "weight": 5, "rarity": "Common"},
    {"name": "Shield", "category": "Armor", "value": 150, "weight": 8, "rarity": "Uncommon"},
    {"name": "Potion", "category": "Consumable", "value": 50, "weight": 1, "rarity": "Common"},
    {"name": "Bow", "category": "Weapon", "value": 120, "weight": 4, "rarity": "Rare"},
    {"name": "Helmet", "category": "Armor", "value": 80, "weight": 3, "rarity": "Uncommon"}
]


def show_items():
    for i, item in enumerate(inventory):
        print(f"{i}: {item}")


def add_item():
    name = input("Name: ")
    category = input("Category: ")
    value = int(input("Value: "))
    weight = int(input("Weight: "))
    rarity = input("Rarity: ")
    inventory.append({"name": name, "category": category, "value": value, "weight": weight, "rarity": rarity})


def update_item():
    index = int(input("Index to update: "))
    if 0 <= index < len(inventory):
        name = input("New name: ")
        category = input("New category: ")
        value = int(input("New value: "))
        weight = int(input("New weight: "))
        rarity = input("New rarity: ")
        inventory[index] = {"name": name, "category": category, "value": value, "weight": weight, "rarity": rarity}
    else:
        print("Invalid index")


def delete_item():
    index = int(input("Index to delete: "))
    if 0 <= index < len(inventory):
        inventory.pop(index)
    else:
        print("Invalid index")


def filter_items():
    cat = input("Category to filter: ")
    for item in inventory:
        if item['category'].lower() == cat.lower():
            print(item)


def main():
    while True:
        print("\n1.Show  2.Add  3.Update  4.Delete  5.Filter  6.Exit")
        choice = input("Choose 1-6: ")
        if choice == "1": show_items()
        elif choice == "2": add_item()
        elif choice == "3": update_item()
        elif choice == "4": delete_item()
        elif choice == "5": filter_items()
        elif choice == "6": break
        else: print("Invalid choice")

if __name__ == "__main__":
    main()