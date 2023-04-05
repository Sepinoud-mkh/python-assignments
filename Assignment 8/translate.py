
def readFromDatabase():
    global dictWords

    data=open("translate.txt")
    info=data.read().split("\n")

    dictWords=[]
    for i in range(0,len(info),2):
        myDictionry={"English":info[i],"Persian":info[i+1]}
        dictWords.append(myDictionry)


    data.close()

def showMenu():
    print("Here is the menu!!\n")
    print("1.Translate from english to persian")
    print("2-Translate from persian to english")
    print("3-Add new words")
    print("4-Exit")

def English_to_Persian():
    userText=input("please enter your english text:")
    userWords=userText.split(" ")
    translation=" "
    for userWord in userWords:
        for word in dictWords:
            if userWord==word["English"]:
                translation=translation+word["Persian"]+" "
                break
        else:
            translation=translation+userWord+" "

    print(translation)

def Persian_to_English():
    userText=input("please enter your english text:")
    userWords=userText.split(" ")
    translation=" "
    for userWord in userWords:
        for word in dictWords:
            if userWord==word["English"]:
                translation=translation+word["Persian"]+" "
                break
        else:
            translation=translation+userWord+" "

    print(translation)



readFromDatabase()
print("Welcome to the translator")
while True:
    showMenu()
    choice=int(input("Please enter your choice:"))

    if choice==1:
        English_to_Persian()
    elif choice==2:
        Persian_to_English()
    elif choice==3:
        ...
    elif choice==4:
        exit(0)