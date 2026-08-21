orders = [
    {"customer": "Ankit", "amount": 1200, "paid": "True"},
    {"customer": "Rohit", "amount": 800, "paid": "False"},
    {"customer": "Vishal", "amount": 2500, "paid": "True"},
    {"customer": "Aman", "amount": 1500, "paid": "False"},
    {"customer": "Neeraj", "amount": 3000, "paid": "True"}
]

for order in orders:
    if order["paid"] == "False":
        print(order["customer"])

for order in orders:
    if order["amount"] > 2000:
        print(order["customer"])

count = 0
for order in orders:
    if order["paid"] == "True":
        count += 1
print(count)

unpaid_orders = []
for order in orders:
    if order["paid"] == "False":
      unpaid_orders.append(order)
print(unpaid_orders)