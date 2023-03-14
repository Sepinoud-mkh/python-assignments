import math

print("Welcome to the cubic equation solver")
print("Enter a,b,c and d parameters")
print("The equetion is ax^3 + bx^2 + cx + d = 0")

def cubic_solve(a,b,c,d):
    z = []
    z.append(1)
    z.append(complex(-5,math.sqrt(3)/2))
    z.append(complex(-5,-1*math.sqrt(3)/2))

    delta = 18*a*b*c*d - 4*b**3*d + b**2*c**2 - 4*a*c**3 - 27*a**2*d**2
    delta0 = b**2 - 3*a*c
    delta1 = 2*b**3 - 9*a*b*c + 27*a**2*d

    S = delta1 + math.sqrt(delta1**2 - 4*delta0**3)
    S = (S/2)**(1/3)

    ans = []
    
    for i in range(3):
        ans = b + z[i]*S + delta0/(z[i]*S)
        ans.append(ans/(-3*a))
    return ans

while True:
    a = float(input("a: "))
    if a == 0.0:
        print("You can't choose zero for a")
    else:
        break

b = float(input("b: "))
c = float(input("c: "))
d = float(input("d: "))

print("{a}x^3 + {b}x^2 + {c}x + {d}".format(a=a,b=b,c=c,d=d))
ans = cubic_solve(a,b,c,d)
for i in range(3):
    print("x{i} = {x}".format(i=i,x=ans[i]))

