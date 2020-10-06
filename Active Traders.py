"""
This is a program to compute which customers are active in 

"""



customers = []

n = len(customers)
customers.sort()
customer_numbers = {}
above_5_customers = []
iternum = len(list(dict.fromkeys(customers)))

for _ in range(iternum):
    for customer in customers:
        count = customers.count(customer)
        customer_numbers[customer] = count
        continue

for customer in customer_numbers:
    if customer_numbers[customer] / n >= .05:
        above_5_customers.append(customer)
    else:
        continue

print(sorted(above_5_customers))
