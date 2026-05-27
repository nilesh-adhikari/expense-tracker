import json

def add_expenses():  
    f = open("expenses.json","w") 
    D={} 
    name = input("enter name of expense=")
    while True:
       try:
              price = int(input("enter price="))
              break
       except ValueError:
              print("enter price in numbers")
    category = input("enter category of expense=")       
    while True:
              try:
                     quantity = int(input("enter number of items="))
                     break
              except ValueError:
                     print("enter a number in quantity")                  

    D["name"] = name
    D["total price"] = price * quantity
    D["category"] = category
    D["quantity"] = quantity 
    L.append(D)
    json.dump(L,f)
    print(L)


def view_expenses():
    f = open("expenses.json","r")
    L = json.load(f)
    print("1.view all expenses")
    print("2.view category wise")
    choose = int(input("enter your choice="))
    if choose==1:
           for i in L:
                  print("name:", i["name"])
                  print("Price:", i["total price"])
                  print("Category:", i["category"])
                  print("Quantity:", i["quantity"])
    elif choose == 2:
        search = input("enter item name or category to search=")
        for i in L:
                if i["name"]==search or i["category"]==search:
                    print(i)

def total_expense():
        f = open("expenses.json","r")
        L = json.load(f)
        total = 0
        print("which category's expenses do u want to know=") 
        print("1.food") 
        print("2.household") 
        print("3.gym") 
        print("4.something else") 
        choose = int(input("enter your choice=")) 
        if choose==1:    
                    for i in L:
                
                        if i["category"] == "food":
                            total += i["total price"]
                    print(total,"total expense of food")

        elif choose == 2:
                        for i in L:
                            if i["category"] == "household":
                                 total += i["total price"]
                        print(total,"total expense of household")

        elif choose == 3:
                         for i in L:
                            if i["category"] == "gym":
                                total += i["total price"]
                         print(total,"total expense of gym")
        elif choose == 4:
                        for i in L:
                            if i["category"] == "something else":
                                    total += i["total price"]
                        print(total,"total expense")
                        
def delete_expense():
       f1= open("expenses.json","r")
       L= json.load(f1)
       f1.close() 
       print("name of data u want to delete")
       name= input("enter name of expense=")
       for i in L:
              if i["name"]== name:
                     L.remove(i)
                   
       f2= open("expenses.json","w")                  
       json.dump(L,f2)
       f2.close()
       print("expense deleted") 

def edit_expenses():    
       print("what do u want to edit?")
       print("1.name")
       print("2.total price")
       print("3.category")
       print("4.quantity")
       choice=int(input("enter your choice="))
       f1 = open("expenses.json","r")
       L = json.load(f1)
       f1.close()
       if choice == 1:
              new_name= input("enter new name")
              for i in L: 
                     i["name"]=new_name 
                     
       elif choice==2:
              new_price= int(input("enter new price"))
              for i in L:
                     i["total price"]= new_price

       elif choice==3:
              new_category= input("enter new category")
              for i in L:
                     i["category"]= new_category
       elif choice==4:
              new_quantity= int(input("enter new quantity"))
              for i in L:
                     i["quantity"]= new_quantity

       f2= open("expenses.json","w")
       json.dump(L,f2)
       f2.close()                                            
                        
def exit():
    print("thanks for using the program")
    

L=[]
decision= input("Y OR N=")
while decision=="Y" or "y": 
        print("1.Add Expenses")
        print("2.View Expenses")
        print("3.Total Expenses")
        print("4.Delete Expenses")
        print("5.Edit Expenses")
        print("6.Exit")

        choice= int(input("enter your choice="))
        if choice==1:
            add_expenses()
        elif choice==2:
            view_expenses()
        elif choice==3:
               total_expense()
        elif choice==4:
               delete_expense() 
        elif choice==5: 
               edit_expenses()            
        elif choice==6:
            exit()
            break 
            decision = N
