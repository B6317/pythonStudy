# coding=utf-8
from __future__ import print_function  # 检测兼容性
from PIL import ImageDraw, ImageFont, Image


def add_font(img):
    draw = ImageDraw.Draw(img)
    my_font = ImageFont.truetype("C:/windows/fonts/Arial.ttf", size=40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 50, 5), '111', font=my_font, fill=fillcolor)  # 第一个参数为x,y位置
    img.save("./result.jpg", "jpeg")
    return 0


if __name__ == '__main__':
    image = Image.open('./test_0.jpg')
    add_font(image)
    image.show()
