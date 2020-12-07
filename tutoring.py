# Ashby Henderson

import csv

def openanewfile(filename=None, file=None):
    if not filename:
        file = open(input('Enter a filename'), 'r')
        return file
    else:
        file = open(filename, 'r')
        return file


def buildcustomerdata(file):
    customer_data = dict()
    lines = [line for line in csv.reader(file)]
    for line in lines:
        cust_num = int(line[0])
        cust_name = line[1]
        cust_balance = float(line[2])
        cust_pass = line[3]

        customer_data[cust_num] = (cust_name, cust_balance, cust_pass)
    return customer_data


def buildproductdata(file):
    productdata = dict()
    lines = [line for line in csv.reader(file)]
    for line in lines:
        itemnum = line[0]
        itemdesc = line[1]
        itemprice = line[2]

        productdata[itemnum] = (itemdesc, itemprice)

    return productdata

def buildtransaction(file):
    """
    CO#####NNNXMMDDYYYY

    :param file:
    :return:
    """
    transaction_data = dict()
    cust_num = None
    cust_ord = 1
    lines = [line.strip() for line in file.readlines()]
    for line in lines:
        if line == 'EOF':
            return transaction_data
        if '^' not in line:

            transaction = line[0:2]  # expandable

            cust_num = int(line[2:7])
            orders = int(line[7:10])
            x = line[10]
            date = formdate(line[11:])


            if cust_num not in transaction_data.keys():
                transaction_data[cust_num] = {cust_ord: {'Invoice Type': x, 'date': date,
                                              'order count': orders, 'orders': {}}}
            else:
                cust_ord = list(transaction_data.keys()).count(cust_num) + 1
                transaction_data[cust_num].update(
                    {cust_ord: {'Invoice Type': x, 'date': date,
                                'order count': orders, 'orders': {}}})

        else:
            quantity, item, date = line.split('^')
            date = formdate(date)
            transaction_data[cust_num][cust_ord]['orders'].update({item: (quantity, date)})




def formdate(date):
    if len(date) != 8:
        return date
    month = date[:2]
    day = date[2:4]
    year = date[4:]
    return '{}/{}/{}'.format(month, day, year)


def validcustomernum(n, cust):
    return n in cust


def validproductnum(n, prods):
    return n in prods


def main():
    """
    # Order Date line:
    #       print("Order Date:{:>15}".format(<you need to fill this in>))
    # Customer line:
    #       print("  Customer:{:>15}{:>30}".format(<you need to fill this in>))
    # Headings line:
    #       print("{:^3}   {:<18}{:<28}{:^10}{:>11}{:>11}{:>14}".format("Ln#","Item #", "Item Description", "Req Date", "Qty","Price", "Total"))
    # Items line:
    #       print("{:^3d}   {:<18}{:<28}{:^10}{:>11d}{:>11.2f}   ${:>10.2f}".format(<you need to fill this in>))
    # Summary line:
    #       print("{:>80}{:>18.2f}".format(<you need to fill this in>))

    local
    26335.75
    27366.85
    53702.60


    accurate
    26335.75
    26851.30
    53187.05
    """

    customer_file = input()
    product_file = input()
    transaction_file = input()

    if True:
        customer_data = buildcustomerdata(openanewfile('customers.csv'))
        product_data = buildproductdata(openanewfile('inventory.csv'))
        transaction_data = buildtransaction(openanewfile('orders.txt'))

    else:
        customer_data = buildcustomerdata(openanewfile(customer_file))
        product_data = buildproductdata(openanewfile(product_file))
        transaction_data = buildtransaction(openanewfile(transaction_file))

    for customer in transaction_data.keys():
        if validcustomernum(customer, list(customer_data.keys())):
            balance = customer_data[customer][1]
            for order in transaction_data[customer]:
                if len(transaction_data[customer].keys()) > 1 and order != 1:
                    balance += running_total
                    print("---------------")
                date = transaction_data[customer][order]['date']
                print("Order Date:{:>15}".format(date))
                print("  Customer:{:>15}{:>30}".format(customer, customer_data[customer][0]))
                if transaction_data[customer][order]['Invoice Type'] == 'D':
                    print("\n{:^3}   {:<18}{:<28}{:^10}{:>11}{:>11}{:>14}".format("Ln#","Item #", "Item Description", "Req Date", "Qty","Price", "Total"))
                count = transaction_data[customer][order]['order count']
                ln = 1
                running_total = 0
                for i in range(count):
                    item = list(transaction_data[customer][order]['orders'].keys())[i]
                    data = transaction_data[customer][order]['orders'][item]
                    if not validproductnum(item, list(product_data.keys())):
                        desc = '*** Item not found ***'
                        price = 0.0
                        total = 0.0
                        running_total = 0.0
                    else:
                        desc = product_data[item][0]
                        price = float(product_data[item][1])
                        total = price * float(data[0])
                        running_total += total
                    if transaction_data[customer][order]['Invoice Type'] == 'D':
                        print("{:^3d}   {:<18}{:<28}{:^10}{:>11d}{:>11.2f}   ${:>10.2f}".format(ln, item, desc, data[1], int(data[0]), price, total))
                    ln += 1
                total_due = running_total + balance
                print("\n{:>80}{:>18.2f}".format('Total Ordered:', running_total))
                print("{:>80}{:>18.2f}".format('Balance:', balance))
                print("\n{:>80}{:>18.2f}".format('Total Due:', total_due))

        else:
            print('Customer number {} is invalid'.format(customer))


if __name__ == '__main__':
    main()
