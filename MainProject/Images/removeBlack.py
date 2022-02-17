
from PIL import Image
from pathlib import Path

result = list(Path(".").rglob("*.[jJ][pP]*"))
for file in result:
    print(file)

    # creating a image object
    # Such as: r"./Ash/ash1.jpg"
    im = Image.open(file)
    px = im.load()

    shouldDelete = 1
    for i in range(17):
#        print (i, px[4, im.height-i-1])
        if px[4, im.height-i-1][0] > 10 or px[4, im.height-i-1][1] > 10 or px[4, im.height-i-1][2] > 10:
            shouldDelete = 0

    print(shouldDelete)

    if shouldDelete:
        im = im.crop((0,0,im.width, im.height-20))
        im.save(file)

#    exit()