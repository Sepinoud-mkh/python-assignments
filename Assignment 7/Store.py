import pyfiglet
import qrcode

PRODUCTS=[]
bill=[]

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

def makeQrCode():
    userInput=input("Enter the code of product")
    for product in PRODUCTS:
        if product["code"]==userInput:
            img=qrcode.make(product)
            img.save("img.png")

def showMenu():
    print("1.ADD")
    print("2.EDIT")
    print("3.REMOVE")
    print("4.SEARCH")
    print("5.SHOW LIST")
    print("6.BUY")
    print("7.QR CODE")
    print("8.EXIT")

def add():
    code=int(input("Please enter the code of product:"))
    name=input("Please enter the name of product:")
    price=int(input("Please enter the price of product:"))
    count=int(input("Please enter the price of product:"))
    new_product={"code":code,"name":name,"price":price,"count":count}
    PRODUCTS.append(new_product)
    print("You added an item successfully!")

def edit():
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
            else:
                print("Please enter correctly")

            print("Data is updated successfully!")
            print("code\tname\tprice\tcount")
            print(product["code"],"\t",product["name"],"\t",product["price"],"\t",product["count"])
            break
        
    else:
        print("Please enter correctly")

def remove():
    userInput=input("Enter the code of the product that you want to remove:")
    for product in PRODUCTS:
        if product["code"]==userInput:
            print("You have chosen %s to be removed"%product["name"])
            PRODUCTS.remove(product)
            print("%s removed successfully"%product["name"])
            break
    else:
        print("The code you entered is not found")

def search():
    userInput=input("Enter the code of the product that you want to search:")
    for product in PRODUCTS:
        if product["code"]==userInput or product["name"]==userInput:
            print(product["code"],"\t",product["name"],"\t",product["price"])
            break
    else:
        print("The entered code is not found")

def showList():
    print("code\tname\tprice")
    for product in PRODUCTS:
        print(product["code"],"\t",product["name"],"\t",product["price"])


def buy():
    total=0
    while True:
        userInput=int(input("Please enter the code of the product"))
        for product in PRODUCTS:
            if product["code"]==userInput:
                num=input("Please enter the count of product")
                count=product["count"]
                if count>=num:
                    count=count-num
                    product["count"]=count
                    product["num"]=num
                    bill.append(product)
                else:
                    print("Out of stock")
            else:
                print("The code you entered is not found")
        ask=input("Do you want to continue?\YES or NO:")
        if ask=="NO":
            print("code\tname\tprice\tnum")
            for item in bill:
                print(item["code"],"\t",item["name"],"\t",item["price"],"\t",item["num"])
                total=total+(int(item["price"])*int(item["num"]))
            sum={"sum":total}
            bill.append(sum)
            print("\tsum=\t",total)
            break

print(pyfiglet.figlet_format("Welcome!",font="bubble"))
print("Loading...")
readFromDatabase()
print("Data Loaded.")
print("Here is the menu.\nWhat do you like to do?\n")
while True:
    showMenu()
    choice=int(input("\nPlease enter your choice:"))
    if choice==1:
        add()
    elif choice==2:
        edit()
    elif choice==3:
        remove()
    elif choice==4:
        search()
    elif choice==5:
        showList()
    elif choice==6:
        buy()
    elif choice==7:
        qrcode()
    elif choice==8:
        writeToDatabase()
        exit(0)
    else:
        print("Incorrect")