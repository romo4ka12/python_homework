name = input("Enter customer name: ")
subtotal = 0.0
count = 0

while True:
    item = input("Enter item name (or 'done' to finish): ")
    if item.upper() == "DONE":
        break

    price = float(input("Enter price: "))
    subtotal += price
    count += 1

print("Customer :", name.upper())
print("Items :", count)
print("Subtotal :", subtotal, "KZT")

hour = int(input("Enter current hour (0-23): "))
print("-" * 30)

if 6 <= hour < 12:
    text = "Morning discount"
    discount = subtotal * 0.10
elif 12 <= hour < 17:
    text = "No discount"
    discount = 0
elif 17 <= hour < 22:
    text = "Evening discount"
    discount = subtotal * 0.05
else:
    print("Closed")
    discount = None

if discount is not None:
    subtotal = subtotal - discount
    tip = subtotal * 0.10
    total = subtotal + tip

    print("Time period :", text)
    print("Discount :", discount, "KZT")
    print("Tip (10%) :", tip, "KZT")
    print("Total :", total, "KZT")
    print("-" * 30)

print("Name uppercase :", name.upper())
print("Name lowercase :", name.lower())
print("Name length :", len(name))

if name[0].upper() == 'A' or name[0].upper() == 'S':
    print("VIP customer")
else:
    print("Regular customer")