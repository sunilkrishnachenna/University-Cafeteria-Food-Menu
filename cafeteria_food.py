import datetime                    
import os                        

food_menu = []                    
drink_beverages = []                        
item_cost_values = [0] * 100                                      
type1_disc = 300                  
type2_disc = 1200                
type3_disc = 5000                
type1_disc_rate = 0.06         
type2_disc_rate = 0.12            
type3_disc_rate = 0.18          
go_link = "/" 
if os.name == "nt":
    go_link = "\\" 

def initial_function():
    global drink_beverages, food_menu, order_of_items, item_cost_values     
    order_of_items = [0] * 100                 
initial_function()                              
                                               
def main_function():
    while True:                                     
        print("(O) ORDER ITEMS \n" "(R) GENERATE REPORT\n" "(P) BILL PAYMENT\n" "(E) EXIT\n")
        user_choice = str(input("Choose Option: ")).upper()   
        if (len(user_choice) == 1):                                      
            if (user_choice == 'O'):                                                              
                food_order_activity()                                       
                break                                                 
            elif (user_choice == 'R'):                                                             
                bill_report_activity()                                   
                break                                            
            elif (user_choice == 'P'):                                                                 
                bill_payment_activity()                                  
                break                                             
            elif (user_choice == 'E'):                                
                print("THANK YOU\n")    
                break                                                    
            else:                                                                                 
                print("ERROR: Invalid Choice")  
        else:                                                                                   
             print("ERROR: Invalid Choice")       

def food_order_activity():                                                                               
    while True:                                            
        print("(F) ORDER OF FOODS AND DRINKS\n" "(M) GO TO MAIN MENU\n" "(E) EXIT\n")
        user_choice = str(input("Choose Option: ")).upper() 
        if len(user_choice) == 1:
            if (user_choice == 'F'):  
                food_drink_order_activity() 
                break
            elif (user_choice == 'M'):
                main_function() 
                break
            elif (user_choice == 'E'):
                print("THANK YOU\n")
                break
            else:
                print("ERROR: Invalid Choice")  
        else:
            print("ERROR: Invalid Choice") 

def total_files_read_activity():                                                                    
    food_menu_read = open('files'+go_link+'food_items.txt', 'r') 
    for i in food_menu_read: 
        food_menu.append(str(i.strip())) 
    food_menu_read.close()

    drink_menu_read = open('files'+go_link+'drink_beverages.txt', 'r') 
    for i in drink_menu_read:
        drink_beverages.append(str(i.strip()))
    drink_menu_read.close()

    i = 0
    while i <= (len(food_menu) - 1): 
        if 'RM' in food_menu[i]:
            food_menu[i] = str(food_menu[i][:food_menu[i].index('RM') - 1]) + ' ' * (20 - (food_menu[i].index('RM') - 1)) + str(food_menu[i][food_menu[i].index('RM'):])
        i += 1

    i = 0
    while i <= (len(drink_beverages) - 1):
        if 'RM' in drink_beverages[i]:
            drink_beverages[i] = str(drink_beverages[i][:drink_beverages[i].index('RM') - 1]) + ' ' * (20 - (drink_beverages[i].index('RM') - 1)) + str(drink_beverages[i][drink_beverages[i].index('RM'):])
        i += 1
total_files_read_activity()

def sort_data_activity(): 
    global food_menu, drink_beverages
    food_menu = sorted(food_menu)
    drink_beverages = sorted(drink_beverages)

    i = 0
    while i < len(food_menu):
        item_cost_values[i] = float(food_menu[i][int(food_menu[i].index("RM") + 3):])
        i += 1

    i = 0
    while i < len(drink_beverages):
        item_cost_values[40 + i] = float(drink_beverages[i][int(drink_beverages[i].index("RM") + 3):]) 
        i += 1

sort_data_activity()

def food_drink_order_activity():
    while True:
            print("Order Food")
            print("FOOD ITEM \t\tCOST \t\tDRINK ITEM \t\tCOST")

            i = 0
            while i < len(food_menu) or i < len(drink_beverages):
                sp = 1
                if i <= 8:                      
                    sp = 2

                if i < len(food_menu):
                    food_val = " (" + str(i + 1) + ")" + " " * sp + str(food_menu[i]) + " | " 
                else:
                    food_val = " " * 36 + "| " 
                if i < len(drink_beverages):
                    drink_val = "(" + str(41 + i) + ")" + " " + str(drink_beverages[i])
                else:
                    drink_val = ""
                print(food_val, drink_val)
                i += 1

            print("\n (M) MAIN MENU \t\t(P) PAYMENT \t\t(E) EXIT\n")

            user_choice = input("Choose Option: ").upper() 
            if (user_choice == 'M'):
                main_function() 
                break
            if (user_choice == 'E'):
                print("THANK YOU\n") 
                break
            if (user_choice == 'P'):
                bill_payment_activity() 
                break
            try:        
                int(user_choice)
                if ((int(user_choice) <= len(food_menu) and int(user_choice) > 0) or (int(user_choice) <= len(drink_beverages) + 40 and int(user_choice) > 40)):
                     try:
                        print("\n" + "_" * 72 + "\n" + str(food_menu[int(user_choice) - 1])) 
                     except:
                        pass
                     try:
                         print("\n" + "_" * 72 + "\n" + str(drink_beverages[int(user_choice) - 41])) 
                     except:
                        pass

                     input_2 = input("Quantity of order items ").upper() 
                     if int(input_2) > 0:
                        order_of_items[int(user_choice) - 1] += int(input_2) 
                        print("Order Completed")
                        food_drink_order_activity() 
                        break
                     else:
                        print("\nInvalid Choice")
            except:
                print("\nERROR: Invalid Choice")

def bill_report_activity():
    while True:
        print("REPORT GENERATION\n")
        report_write = open('files'+go_link+'report.txt', 'r').read() 
        print(report_write)
        print("\n(M) GO TO MAIN MENU \t\t(E) EXIT\n")
        user_choice = str(input("Choose Option: ")).upper()
        if (user_choice == 'M'):
            main_function() 
            break
        elif (user_choice == 'E'):
            print("THANK YOU\n") 
            break
        else:
            print("\nERROR: Invalid Choice")

def bill_payment_activity():
    while True:
        print("BILL PAYMENT\n")
        items_bill = 0 
        generate_update_bill = "\n DATE: " + str(datetime.datetime.now())[:19] + "\n"
        i = 0
        while i < len(order_of_items): 
            if(order_of_items[i] != 0):
                if (i >= 0) and (i < 40):
                    generate_update_bill += "\n" + " " * 17 + str(food_menu[i]) + "  x  " + str(order_of_items[i]) 
                    print(" " * 17 + str(food_menu[i]) + "  x  " + str(order_of_items[i])) 
                    items_bill += item_cost_values[i] * order_of_items[i] 
                if (i >= 40) and (i < 80):
                    generate_update_bill += "\n" + " " * 17 + str(drink_beverages[i - 40]) + "  x  " + str(order_of_items[i])
                    print(" " * 17 + str(drink_beverages[i - 40]) + "   x  " + str(order_of_items[i]))
                    items_bill += item_cost_values[i] * order_of_items[i] 
                i += 1
            else:
                i += 1
        
        if items_bill > type3_disc: 
            items_bill -= items_bill * type3_disc_rate 
            generate_update_bill += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "RATE OF DISCOUNT:      % " + str(type3_disc_rate * 100) + "\n" \
                "" + " " * 17 + "COST OF DISCOUNT:   RM " + str(round(items_bill * type3_disc_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "PAID BIULL:       RM " + str(round(items_bill, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "RATE OF DISCOUNT:      % " + str(type3_disc_rate * 100) + "\n"
                "" + " " * 17 + "COST OF DISCOUNT:   RM " + str(round(items_bill * type3_disc_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "PAID BIULL:        RM " + str(round(items_bill, 2)))
        elif items_bill > type2_disc: 
            items_bill -= items_bill * type2_disc_rate 
            generate_update_bill += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "RATE OF DISCOUNT:      % " + str(type2_disc_rate * 100) + "\n" \
                "" + " " * 17 + "COST OF DISCOUNT:   RM " + str(round(items_bill * type2_disc_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "PAID BIULL:        RM " + str(round(items_bill, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "RATE OF DISCOUNT:      % " + str(type2_disc_rate * 100) + "\n"
                "" + " " * 17 + "COST OF DISCOUNT:   RM " + str(round(items_bill * type2_disc_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "PAID BIULL:        RM " + str(round(items_bill, 2)))
        elif items_bill > type1_disc: 
            items_bill -= items_bill * type1_disc_rate 
            generate_update_bill += "\n" + " " * 17 + "-" * 35 + "\n" \
                "" + " " * 17 + "RATE OF DISCOUNT:      % " + str(type1_disc_rate * 100) + "\n" \
                "" + " " * 17 + "COST OF DISCOUNT:   RM " + str(round(items_bill * type1_disc_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n" \
                "" + " " * 17 + "PAID BIULL:        RM " + str(round(items_bill, 2)) + "\n" + " " * 17 + "*" * 35 
            print(" " * 17 + "-" * 35 + "\n"
                "" + " " * 17 + "RATE OF DISCOUNT:      % " + str(type1_disc_rate * 100) + "\n"
                "" + " " * 17 + "COST OF DISCOUNT:   RM " + str(round(items_bill * type1_disc_rate, 2)) + "\n" + " " * 17 + "_" * 35 + "\n"
                "" + " " * 17 + "PAID BIULL:       RM " + str(round(items_bill, 2)))
        else:
            generate_update_bill += "\n" + " " * 17 + "-" * 35 + "\n" + " " * 17 + "ITEMS COST:       RM " + str(round(items_bill, 2)) + "\n" + " " * 17 + "*" * 35
            print(" " * 17 + "_" * 35 + "\n" + " " * 17 + "ITEMS COST:       RM " + str(round(items_bill, 2)))

        print("\n (P) PAY BILL \t\t(M) GO TO MAIN MENU \t\t(R) GENERATE REPORT  \t\t(E) EXIT\n" + "_" * 72)
        user_choice = str(input("Choose Option: ")).upper()
        if (user_choice == 'P'):
            print("Bill Payment Coimpleted")
            report_write = open('files'+go_link+'report.txt', 'a') 
            report_write.write(generate_update_bill)
            report_write.close()
            initial_function() 
        elif (user_choice == 'M'):
            main_function() 
            break
        elif (user_choice == 'R'):
            bill_report_activity() 
            break
        elif ('E' in user_choice) or ('e' in user_choice):
            print("THANK YOU\n")
            break
        else:
            print("\nERROR: Invalid Choice")
main_function() 
