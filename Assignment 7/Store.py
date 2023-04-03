import pyfiglet
#import qrcode

PRODUCTS=[]

def readFromDatabase():
    data=open("database.txt","r")
    for line in data:
        result=line.split(",")
        info={"code":result[0],"name":result[1],"price":result[2],"count":result[3]}
        PRODUCTS.append(info)
    
    data.close()

def writeToDatabase():
    data=open("database.txt","w")
    data=open("database.txt","a")
    for product in PRODUCTS:
        line=str(product["code"])+","+product["name"]+","+str(product["price"])+","+str(product["count"])
        data.write(line.strip()+"\n")
    data.close()

#def makeQrCode():
#    user_input=input("Enter the code of ")

def show_menu():
    print("1.ADD")
    print("2.EDIT")
    print("3.REMOVE")
    print("4.SEARCH")
    print("5.SHOW LIST")
    print("6.BUY")
    print("7.EXIT")

print(pyfiglet.figlet_format("Welcome!",font="bubble"))
print("Loading...")
readFromDatabase()
print("Data Loaded.")
print("Here is the menu.\nWhat do you like to do?\n")
show_menu()
choice=int(input("\nPlease enter your choice:"))

#Add:
if choice==1:
    code=int(input("Please enter the code of product:"))
    name=input("Please enter the name of product:")
    price=int(input("Please enter the price of product:"))
    count=int(input("Please enter the price of product:"))
    new_product={"code":code,"name":name,"price":price,"count":count}
    PRODUCTS.append(new_product)
    print("You added an item successfully!")

#Edit:
elif choice==2:
    print("You wanted to edit a product")
    userInput=input("Enter the code of the product that you wanted to edit:")
    for product in PRODUCTS:
        if product["code"]==userInput:
            print("You have chosen %s to be edited:"%product["name"])
        
            print("Which info would like to edit?")
            print("1-Name\n2-Price\n3-Count")
        
            choice=int(input("Please enter your choice:"))
        
            if choice==1:
                new_name=input("Please enter the new name of product:")
                product["name"]=new_name
            elif choice==2:
                new_price=input("Please enter the new price of product:")
                product["price"]=new_price
            elif choice==3:
                new_count=input("Please enter the new count of product:")
                product["count"]=new_count

            print("Data is updated successfully!")
            print("code\tname\tprice\tcount")
            print(product["code"],"\t",product["name"],"\t",product["price"],"\t",product["count"])
            break
        
        else:
            print("Please enter correctly")

#Remove:    
elif choice==3:
    ...

#Search:
elif choice==4:
    ...

#Show List
elif choice==5:
    print("code\tname\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t",product["name"],"\t",product["price"])

#Buy:
elif choice==6:
    ...

#Exit:    
elif choice==7:
    exit()

else:
    print("Please enter correctly!!")
