# coding=utf-8
# create by toonew at 2018/2/27


class TestClass:
    def __init__(self, right, left):
        self.r = right
        self.l = left

    _i = 0          # python没有java那种完全私有变量，只有语义上的私有变量
    i = 12345       # python也没有java static 静态变量这个概念

    def f(self):
        return "hello world"


if __name__ == "__main__":
    t = TestClass(3.0, -4.5)
    print(t.i)
    t.i = t.i + 1
    print(t._i)
    print(t.f())
    print(t.r, t.l)

    t2 = TestClass(4, -4)
    print(t.i)
