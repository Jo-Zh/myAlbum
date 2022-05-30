
def order_food_while_cond(menu):
    orders=[]
    order=input('What would you like to order? (Q to Quit')
    
    while (order.upper() != 'Q') :
        if menu.get(order):
            orders.append(order)
        else:
            print("Oder doesn't exist")
        
        order=input("Anything else? (Q to Quit)")

    
    return orders
    
    
def order_food_while_true(menu):
    orders=[]
    order=input('What would you like to order? (Q to Quit)')
    
    while (True):
    
        if order.upper() == 'Q' :
            break
            
        elif order == 'CheekySpam':
            print("Sorry, we're all out of that!")
            order=input("Anything else? (Q to Quit)")
            continue
            
        elif menu.get(order):
            orders.append(order)
            
        else:
            print("Oder doesn't exist")
        
        order=input("Anything else? (Q to Quit)")

    return orders
    
def total_price(orders,menu):
    total=0
    for order in orders:
        total+=float(menu[order].replace('$', ''))
    return total

def write_sales_log(orders, total, menu):
    file=open('salse.txt', 'w')
    for order in orders:
        order_item=menu[order]
        file.write(order+'\n')
    file.write(str(total)+'\n\t')    
    file.close()

def main(menu):
    orders=order_food_while_true(menu)
    total=total_price(orders,menu)
    return write_sales_log(orders, total,menu)
    
menu={'A':"2$", 'B':"3$", "chips": "4$"}
    
if __name__=="__main__":
    
    main(menu)
