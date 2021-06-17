import numpy as np
from PIL import Image
from os import listdir
from os.path import isfile, join

def makeTransparent(file, threshold = 140, dist = 20):
    img = Image.open(file)
    img = img.convert("RGBA")
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] >= threshold and item[1] >= threshold and item[2] >= threshold \
            and abs(item[0]-item[1]) <=dist and abs(item[0]-item[2]) <=dist and abs(item[1]-item[2]) <=dist:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    img.save("transparent_" + file + ".png", "PNG")
    print("File " + file + " converted.")

for file in [f for f in listdir("./") if (f.endswith("jpg") and isfile(join("./", f)))]:
    makeTransparent(file)
