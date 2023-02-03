import qrcode
name=input("Enter your name:")
phonenumber=input("Enter your phone number:")
code=qrcode.make(name+" "+phonenumber)
code.save("qrcode.png")