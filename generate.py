from PIL import Image

import random
import sys


image = Image.open(sys.argv[1])
image = image.convert('1')

outfile1 = Image.new("1", [dimension * 2 for dimension in image.size])

outfile2 = Image.new("1", [dimension * 2 for dimension in image.size])

for x in range(0, image.size[0], 2):
    for y in range(0, image.size[1], 2):
        sourcepixel = image.getpixel((x, y))
        assert sourcepixel in (0, 255)
        coinflip = random.random()
        if sourcepixel == 0:
            if coinflip < .5:
                outfile1.putpixel((x * 2, y * 2), 255)
                outfile1.putpixel((x * 2 + 1, y * 2), 0)
                outfile1.putpixel((x * 2, y * 2 + 1), 0)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 255)
                
                outfile2.putpixel((x * 2, y * 2), 0)
                outfile2.putpixel((x * 2 + 1, y * 2), 255)
                outfile2.putpixel((x * 2, y * 2 + 1), 255)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 0)
            else:
                outfile1.putpixel((x * 2, y * 2), 0)
                outfile1.putpixel((x * 2 + 1, y * 2), 255)
                outfile1.putpixel((x * 2, y * 2 + 1), 255)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 0)
                
                outfile2.putpixel((x * 2, y * 2), 255)
                outfile2.putpixel((x * 2 + 1, y * 2), 0)
                outfile2.putpixel((x * 2, y * 2 + 1), 0)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 255)
        elif sourcepixel == 255:
            if coinflip < .5:
                outfile1.putpixel((x * 2, y * 2), 255)
                outfile1.putpixel((x * 2 + 1, y * 2), 0)
                outfile1.putpixel((x * 2, y * 2 + 1), 0)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 255)
                
                outfile2.putpixel((x * 2, y * 2), 255)
                outfile2.putpixel((x * 2 + 1, y * 2), 0)
                outfile2.putpixel((x * 2, y * 2 + 1), 0)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 255)
            else:
                outfile1.putpixel((x * 2, y * 2), 0)
                outfile1.putpixel((x * 2 + 1, y * 2), 255)
                outfile1.putpixel((x * 2, y * 2 + 1), 255)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 0)
                
                outfile2.putpixel((x * 2, y * 2), 0)
                outfile2.putpixel((x * 2 + 1, y * 2), 255)
                outfile2.putpixel((x * 2, y * 2 + 1), 255)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 0)

outfile1.save('out1.jpg')
outfile2.save('out2.jpg')
