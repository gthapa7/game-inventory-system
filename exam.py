inventory = [
    {"name": "Sword", "category": "Weapon", "value": 100},
    {"name": "Shield", "category": "Armor", "value": 150},
    {"name": "Potion", "category": "Consumable", "value": 50},
    {"name": "Bow", "category": "Weapon", "value": 120},
    {"name": "Helmet", "category": "Armor", "value": 80}
]

def show_all(ls):
    for i, item in enumerate(ls):
        print(f"Index {i}: {item}")

def add(ls):
    name = input("Enter Name: ")
    category = input("Enter Category: ")
    value = int(input("Enter Value: "))
    ls.append({"name": name, "category": category, "value": value})

def delete(ls):
    show_all(ls)
    i = int(input("Delete at Index: "))
    if i in range(len(ls)):
        ls.pop(i)
    else:
        print("Enter a valid index")

def update(ls):
    show_all(ls)
    index = int(input("Update at index: "))
    if index in range(len(ls)):
        item = ls[index]
        new_name = input("Updated Name: ")
        if new_name:
            item["name"] = new_name
        new_category = input("Updated Category: ")
        if new_category:
            item["category"] = new_category
        val = input("Updated Value: ")
        if val:
            item["value"] = int(val)
    else:
            print("Invalid index")

def merge_sort(items, sort_by_1, sort_by_2):
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid], sort_by_1, sort_by_2)
    right = merge_sort(items[mid:], sort_by_1, sort_by_2)

    return merge(left, right, sort_by_1, sort_by_2)

def merge(left, right, sort_by_1, sort_by_2):
    sorted_list = []
    while left and right:
        if (left[0][sort_by_1], left[0][sort_by_2]) <= (right[0][sort_by_1], right[0][sort_by_2]):
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))
    sorted_list.extend(left or right)
    return sorted_list

def bubble_sort(ls, sort_by_1, sort_by_2):
    n = len(ls)
    for i in range(n):
        for j in range(0, n - i - 1):
            a, b = ls[j], ls[j + 1]
            if a[sort_by_1] > b[sort_by_1] or (a[sort_by_1] == b[sort_by_1] and a[sort_by_2] > b[sort_by_2]):
                ls[j], ls[j + 1] = ls[j + 1], ls[j]
    return ls

def sort(ls, sort_by_1, sort_by_2, memory_threshold):
    if len(ls) < memory_threshold:
        print("Sorted using Merge Sort: ")
        ls = merge_sort(ls, sort_by_1, sort_by_2)
    else:
        print("Sorted using Bubble Sort: ")
        ls = bubble_sort(ls, sort_by_1, sort_by_2)
    return ls

def linear_search(ls, search_param):
    search_item = input("Enter item to search for: ")
    found = False
    for item in ls:
        if item[search_param].lower() == search_item:
            print(f"Name: {item['name']}, Category: {item['category']}, Value: {item['value']}")
            found = True
    if not found:
        print("No " + f"{search_item}" + " found in " + f"{search_param}")

def main():
    while True:
        print("\n1. Show Inventory\n2. Add Item\n3. Delete Item\n4. Update Item\n5. Sort Inventory\n6. Search Item by name/category\n0. Exit")
        choice = input("Choose: ")
        if choice == '1':
            show_all(inventory)
        elif choice == '2':
            add(inventory)
        elif choice == '3':
            delete(inventory)
        elif choice == '4':
            update(inventory)
        elif choice == '5':
            sort_by_1 = input("First Sort by: ")
            sort_by_2 = input("Then Sort by: ")
            memory_threshold = 500
            show_all(sort(inventory, sort_by_1, sort_by_2, memory_threshold))
        elif choice == '6':
            search_param = input("Search attribute: ")
            linear_search(inventory,search_param)
        elif choice == '0':
            print("Exiting...")
            break
        else:
            print("Invalid choice")

main()