# coding=utf-8
# create by toonew at 2018/1/28
from __future__ import print_function

import random
import string
from os import listdir
from os.path import isfile, join

from PIL import ImageDraw, Image

mypath = '/Users/toonew/test'

onlyfiles = [join(mypath, f) for f in listdir(mypath) if isfile(join(mypath, f))]


def change_size(img_path):
    img = Image.open(img_path)
    resized = img.resize((640, 1136), resample=Image.LANCZOS)
    resized.save("./test/result" + "".join(random.sample(string.digits, 3)) + '.jpg', format="jpeg")


print(onlyfiles)
for imgPath in onlyfiles:
    change_size(imgPath)
