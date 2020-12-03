items_num = int(input("Number of items: "))
while items_num < 0:
    print("Invalid number of items!")
    items_num = int(input("Number of items: "))
total_price = 0
for i in range(items_num):
    item_price = float(input("Price of item: "))
    total_price = total_price + item_price
if total_price > 100:
    total_price = total_price * 0.9
print("Total price for %d items is $%.2f" % (items_num, total_price))
