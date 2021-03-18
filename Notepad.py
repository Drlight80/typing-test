def sh(x):
    """    list__ = []

    class struct:
        def __init__(self, path):
            self.path = path

        def Struct(self):
            file = open(self.path, 'r')
            for i3 in file:
                list__.append(i3)

    s = struct("F:\\tester.txt")
    s.Struct()"""

    class draw:
        import turtle
        sc = turtle.Screen()
        t = turtle.Turtle()
        t.ht()

        def __init__(self, lenght=600, width=500):
            self.lenght = lenght
            self.width = width

        def screen(self, bgcolor='white'):
            self.bgcolor = bgcolor
            self.turtle.title("AMIR Hossein : DR Light")
            self.turtle.bgcolor(self.bgcolor)
            self.sc.setup(self.lenght, self.width)

        t.penup()
        t.goto(165, 155)
        t.pendown()

        def write(self, txt, move=False, pencolor='blue', font=('Arial', 12, 'normal'), goto=()):
            self.t.penup()
            self.t.goto(goto)
            self.t.pendown()
            self.t.pencolor(pencolor)
            self.t.write(txt, move=move, align='right', font=font)

    list_ = []  # for save txt with \n (the texts with 71 character)

    def __txt__(txt):
        print(txt)
        counter = 0  # for limit of character
        n = 0  # for range of  71 character for example 71*n
        for i in txt:
            counter += 1
            if counter == 68:  # original is 71
                if ' ' in txt[67:68:]:  # the latest
                    list_.append('{}\n'.format(txt[68 * n:68 * (n + 1):]))
                if ' ' not in txt[67:68:]:
                    _counter_ = 0
                    while True:
                        x = 67 - _counter_
                        y = 68 - _counter_
                        if ' ' in txt[x:y:]:
                            xx = (68 * n) - _counter_
                            yy = (68 * (n + 1)) - _counter_
                            if n == 0:
                                xx = 68 * n
                            list_.append('{}\n'.format(txt[xx:yy:]))
                            break
                        _counter_ += 1
                n += 1
                counter = 0
                continue
        list_.append(txt[68 * n::])
        # list_.append('\n')
        return 0

    screen = draw(500, 400)
    screen.screen('black')
    counter = 165

    __txt__(x)

    for ii in list_:
        counter -= 28
        screen.write(txt=ii, pencolor='yellow', goto=(165, counter))
    list_.clear()
