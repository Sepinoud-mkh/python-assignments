
def readDatabase():
    global dictionaryWords

    data=open("translate.txt")
    info=data.read().split("\n")
    
    dictionaryWords=[]
    for i in range(0,len(info),2):
        myDictionary={"English":info[i],"Persian":info[i+1]}
        dictionaryWords.append(myDictionary)

    data.close()

def showMenu():
    print("\nHere is the menu!!\n")
    print("1.Translate")
    print("2-Add new words")
    print("3-Exit")

def translate(text,wantedLanguage):
    translation=""

    if wantedLanguage=="persian" or wantedLanguage=="Persian":
        userWords=text.split(" ")
        for userWord in userWords:
            for word in dictionaryWords:
                if userWord==word["English"]:
                    translation=translation+word["Persian"]+" "
                    break
            else:
                translation=translation+userWord+" "
        print("The translation is:%s"%translation)
    
    elif wantedLanguage=="english" or wantedLanguage=="English":
        userWords=text.split(" ")
        for userWord in userWords:
            for word in dictionaryWords:
                if userWord==word["Persian"]:
                    translation=translation+word["English"]+" "
                    break
            else:
                translation=translation+userWord+" "

        print("The translation is:%s"%translation)

def writeToDatabase():
    userNewWordEN=input("Enter the word in english:")
    userNewWordPer=input("Enter the word in persian:")
    newDict={"English":userNewWordEN,"Persian":userNewWordPer}
    dictionaryWords.append(newDict)

readDatabase()
while True:
    showMenu()
    choice=int(input("Please enter your choice:"))
    if choice==1:
        userText=input("Please enter your Text:")
        userLanguage=input("Please enter the Language that you want your text to be translated into:")
        translate(userText,userLanguage)
    elif choice==2:
        writeToDatabase()
    elif choice==3:
        exit(0)

