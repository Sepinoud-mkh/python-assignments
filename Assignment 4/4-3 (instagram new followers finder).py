from getpass import getpass
import instaloader

username=input("Enter your username:")
password=getpass("Enter your password:")

L=instaloader.Instaloader()
L.login(username, password)
profile=instaloader.Profile.from_username(L.context, "sajjad_aemmi")

f=open("followers.txt", "r")
oldFollowers=[]
for line in f:
    oldFollowers.append(line.strip())
f.close()

newFollowers=[]
for follower in profile.getFollowers():
    newFollowers.append(follower.username)

for newFollower in newFollowers:
    if newFollower not in oldFollowers:
        print(newFollower)

f=open("followers.txt", "w")
for newFollower in newFollowers:
    f.write(newFollower + "\n")
f.close()