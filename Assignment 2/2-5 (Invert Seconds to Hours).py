seconds=int(input())
h=int(seconds//3600)
m=int(seconds%3600)//60
s=int(seconds%3600)%60
print("%.2d"%h,"%.2d"%m,"%.2d"%s,sep=":")