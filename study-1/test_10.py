# coding=utf-8
# create by toonew at 2018/1/30
import platform
import random
import string
import os

from PIL import Image, ImageFont, ImageDraw, ImageFilter


def select_font_path():
    sys_str = platform.system()
    if sys_str == 'Windows':
        return "C:/windows/fonts/Arial.ttf"
    elif sys_str == "Darwin":
        return "/Library/Fonts/Skia.ttf"
    elif sys_str == 'Linux':
        return None
    else:
        return None


# 字体的位置，不同版本的系统会有不同
font_path = select_font_path()

# 生成验证码位数
number = 4
# 背景颜色，默认为白色
bg_color = (255, 255, 255)
# 字体颜色，默认为蓝色
font_color = (0, 0, 255)
# 干扰线颜色，默认为红色
line_color = (255, 0, 0)
# 是否加入干扰线
draw_line = True


def gene_text():
    source = string.lowercase + string.uppercase + string.digits
    return "".join(random.sample(source, number))


def gene_code(text, path):
    width, height = 100, 50  # 宽和高
    image = Image.new("RGBA", (width, height), bg_color)  # 创建图片
    font = ImageFont.truetype(font_path, 25)  # 验证码字体和字体大小
    font_width, font_height = font.getsize(text)
    draw = ImageDraw.Draw(image)  # 创建画笔
    draw.text(((width - font_width) / number, (height - font_height) / number), text,
              font=font, fill=font_color)  # 填充字符串

    if draw_line:
        gene_line(draw, width, height)

    # image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
    image.save(path)  # 保存验证码图片


def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=line_color)


if __name__ == "__main__":
    if not os.path.exists("./test"):
        os.mkdir('./test')
    gene_code(gene_text(), './test/idencode.png')
