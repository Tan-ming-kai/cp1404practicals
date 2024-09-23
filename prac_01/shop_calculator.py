number_of_items= int(input("Enter the number of items: "))
total_cost_of_items = []
total = 0

while number_of_items<=0:
    print("Please enter a valid number of items")
    number_of_items = int(input("Enter the number of items: "))

while number_of_items> 0:
    for i in range(number_of_items):
        price_of_item=float(input("Enter the item price: "))
        total_cost_of_items.append(price_of_item)
        total = price_of_item+total
    if total > 100:
        total=total*0.9
    print(f"Total price for {number_of_items} items is ${total:.2f}")

