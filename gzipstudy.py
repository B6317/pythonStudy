import gzipstudy


def ungzip(data):
    try:
        print('正在尝试解压.....')
        data = gzipstudy.decompress(data)
        print('解压完毕')
    except:
        print('无需解压')
    return data
