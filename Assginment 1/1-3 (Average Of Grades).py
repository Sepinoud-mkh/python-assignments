first_Name,last_Name=map(str,(input("enter first name and last name:")).split())
g1,g2,g3=map(int,(input("enter grades:")).split())
average=(float(g1+g2+g3)/3)
if average >= 17 :
    print("Great")
elif 17 > average >= 12 :
    print("Normal")
elif average < 12 :
    print("Fail")