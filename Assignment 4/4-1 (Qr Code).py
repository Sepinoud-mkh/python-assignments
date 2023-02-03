import qrcode
name,phonenumber=map(str,input("Enter your name:\nEnter your phone number:").split("\n"))
code=qrcode.make(name+phonenumber)
code.save("qrcode.png")