import math

one_Input_Op=["sqrt","sin","cos","tan","cot","factorial"]

print("Welcome!")
print("+:sum\n-:sub\n*:mul\n/:div\n^:power\nsqrt:square root\nsin:sinus\ncos:cosinus\ntan:tangent\ncot:cotangent\n!:factorial")
print("Please enter your choice:")

while True:
    Op=input()
    if Op=="exit":
        break
    elif Op in one_Input_Op:
        num_1=float(input())
    else:
        num_1=float(input())
        num_2=float(input())
    if Op=="+":
        result=num_1 + num_2
    elif Op=="-":
        result=num_1 - num_2
    elif Op=="/":
        if num_2!="0": 
            result=num_1/num_2
        else:
            result="Can't divide by zero"
    elif Op=="^":
        result=num_1 ** num_2
    elif Op=="sqrt":
        result=math.sqrt(num_1)
    elif Op=="sin":
        result=math.sin((num_1*180)/math.pi)
    elif Op=="cos":
        result=math.cos((num_1*180)/math.pi)
    elif Op=="tan":
        result=math.tan((num_1*180)/math.pi)
    elif Op=="cot":
        result=math.cot((num_1*180)/math.pi)
    elif Op=="factorial":
        result=math.factorial(num_1)

    print("The result is:",result)