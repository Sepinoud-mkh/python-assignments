w=int(input("enetr your weight:"))
h=float(input("enter your height"))
if (w/(h*h))< 18.5 :
    print("Underweight")
elif 18.5 < (w/(h*h)) < 24.9:
    print("Normal Weight")
elif 25 < (w/(h*h)) < 29.9:
    print("Overweight")
elif 30 < (w/(h*h)) < 34.9:
    print("Obesity")
elif 35 < (w/(h*h)) < 39.9 :
    print("Extreme Obesity")