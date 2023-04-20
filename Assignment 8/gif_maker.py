import os
import imageio

fileList = sorted(os.listdir("gifFolder"))
IMAGES =[]

for fileName in fileList:
    filePath = "gifFolder/" + fileName
    image = imageio.imread(filePath)
    IMAGES.append(image)

imageio.mimsave("myGif.gif", IMAGES, fps=10)