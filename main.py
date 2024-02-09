from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.colorchooser import askcolor
import turtle
from PIL import ImageGrab
import colorsys
import random

class Paint(object):

    DEFAULT_PEN_SIZE = 5.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()
        self.root.title('Python Painter')                                        # Pidugu Jatin  21100BTCSE09917
        menubar =Menu(self.root)
        self.root.config(menu=menubar)
        fileMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=fileMenu)
        fileMenu.add_command(label="Save" , command=self.save_drawing)
        fileMenu.add_command(label="Reset", command=self.reset )
        fileMenu.add_command(label="Exit", command=self.exit)

        designMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Design", menu=designMenu)
        designMenu.add_command(label="Design_1", command=self.design_1)
        designMenu.add_command(label="Design_2", command=self.design_2)
        designMenu.add_command(label="Design_3", command=self.design_3)
        designMenu.add_command(label="Design_4", command=self.design_4)
        designMenu.add_command(label="Design_5", command=self.design_5)
        designMenu.add_command(label="Design_6", command=self.design_6)
        designMenu.add_command(label="Astroid", command=self.design_8)
        designMenu.add_command(label="Triad", command=self.design_9)
        designMenu.add_command(label="Squard", command=self.design_10)
        designMenu.add_command(label="Pentagon", command=self.design_11)
        designMenu.add_command(label="Octagon", command=self.design_12)

        mandelMenu = Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Mandel", menu=mandelMenu)
        mandelMenu.add_command(label="Mandel_1" , command=self.mandel_1)
        mandelMenu.add_command(label="Mandel_2" , command=self.mandel_2)
        mandelMenu.add_command(label="Mandel_3" , command=self.mandel_3)
        mandelMenu.add_command(label="Mandel_4", command=self.mandel_4)
        mandelMenu.add_command(label="Mandel_5", command=self.mandel_5)
        mandelMenu.add_command(label="Mandel_6", command=self.mandel_6)

        self.pen_button = Button(self.root, text='pen', command=self.use_pen)
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='Brush', command=self.use_brush)
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='color', command=self.choose_color)
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='eraser', command=self.use_eraser)
        self.eraser_button.grid(row=0, column=3)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=HORIZONTAL)
        self.choose_size_button.grid(row=0, column=4)

        self.c = Canvas(self.root, bg='white', width=720, height=720)
        self.c.grid(row=1, columnspan=6)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)

    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False, ):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y, width=self.line_width, fill=paint_color, capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

    def exit(self):                                                          #siddharth Sharma   2010DMTCSE07173
        win = Tk()
        win.quit()

    def save_drawing(self):                                                  #Akshat Shukla  2010DMTCSE07742
        try:
            file_ss = filedialog.asksaveasfilename(defaultextension='jpg')
            x = self.root.winfo_rootx() + self.background.winfo_x()
            y = self.root.winfo_rooty() + self.background.winfo_y()
            x1 = x + self.background.winfo_width()
            y1 = y + self.background.winfo_height()
            ImageGrab.grab().crop((x, y, x1, y1)).save(file_ss)
            messagebox.showinfo('Screenshot Successfully Saved as' + str(file_ss))
        except:
            print("Error in saving the screeshoot")

    def design_1(self):                                              # done By Pidugu Jatin
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c )
        spiral = tur
        for i in range(20):
            spiral.forward(i * 10)
            spiral.right(144)
        spiral.write("Done BY Pidugu Jatin")

    def design_2(self):
        self.screen = turtle.TurtleScreen(self.c)                   #Anjili Jain      2010DMTCSE07746
        tur = turtle.RawTurtle(self.c)
        t = tur
        t.color("#ffcc00")
        t.pensize(2)
        t.speed(0)
        def pen(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
        def pattern():
            for i in range(23):
                t.forward(360)
                t.circle(20)
                t.left(216 + 3)
        def star():
            t.begin_fill()
            for i in range(9):
                t.forward(80)
                t.left(160)
            t.end_fill()
        pen(-200, 100)
        pattern()
        pen(-30, -184)
        t.circle(220)
        pen(-30, -194)
        t.circle(230)
        pen(-30, -144)
        t.circle(180)
        pen(-60, 30)
        star()
        pen(-21, -10)
        t.circle(46)
        t.write("Done By Anjili Jain ")
        t.hideturtle()

    def design_3(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)
        roo = tur                                             #Pidugu Jatin 21100BTCSE09917
        roo.left(0)
        roo.speed(0)
        def draw(l):
            if l < 10:
                return
            else:
                roo.pensize(2)
                roo.pencolor("yellow")
                roo.forward(l)
                roo.left(30)
                draw(3 * l / 4)
                roo.right(60)
                draw(3 * l / 4)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(20)
        roo.right(90)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor("magenta")  # magenta
                roo.forward(l)
                roo.left(30)
                draw(3 * l / 4)
                roo.right(60)
                draw(3 * l / 4)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(20)
        roo.left(270)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor("red")  # red
                roo.forward(l)
                roo.left(30)
                draw(3 * l / 4)
                roo.right(60)
                draw(3 * l / 4)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(20)
        roo.right(90)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor('#FFF8DC')  # white
                roo.forward(l)
                roo.left(30)
                draw(3 * l / 4)
                roo.right(60)
                draw(3 * l / 4)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(20)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(3)
                roo.pencolor("lightgreen")  # lightgreen
                roo.forward(l)
                roo.left(30)
                draw(4 * l / 5)
                roo.right(60)
                draw(4 * l / 5)
                roo.left(30)
                roo.pensize(3)
                roo.backward(l)
        draw(40)
        roo.right(90)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(3)
                roo.pencolor("red")  # red
                roo.forward(l)
                roo.left(30)
                draw(4 * l / 5)
                roo.right(60)
                draw(4 * l / 5)
                roo.left(30)
                roo.pensize(3)
                roo.backward(l)
        draw(40)
        roo.left(270)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(3)
                roo.pencolor("yellow")  # yellow
                roo.forward(l)
                roo.left(30)
                draw(4 * l / 5)
                roo.right(60)
                draw(4 * l / 5)
                roo.left(30)
                roo.pensize(3)
                roo.backward(l)
        draw(40)
        roo.right(90)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(3)
                roo.pencolor('#FFF8DC')  # white
                roo.forward(l)
                roo.left(30)
                draw(4 * l / 5)
                roo.right(60)
                draw(4 * l / 5)
                roo.left(30)
                roo.pensize(3)
                roo.backward(l)
        draw(40)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor("cyan")  # cyan
                roo.forward(l)
                roo.left(30)
                draw(6 * l / 7)
                roo.right(60)
                draw(6 * l / 7)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(60)
        roo.right(90)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor("yellow")  # yellow
                roo.forward(l)
                roo.left(30)
                draw(6 * l / 7)
                roo.right(60)
                draw(6 * l / 7)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(60)
        roo.left(270)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor("magenta")  # magenta
                roo.forward(l)
                roo.left(30)
                draw(6 * l / 7)
                roo.right(60)
                draw(6 * l / 7)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
        draw(60)
        roo.right(90)
        roo.speed(0)
        def draw(l):
            if (l < 10):
                return
            else:
                roo.pensize(2)
                roo.pencolor('#FFF8DC')  # white
                roo.forward(l)
                roo.left(30)
                draw(6 * l / 7)
                roo.right(60)
                draw(6 * l / 7)
                roo.left(30)
                roo.pensize(2)
                roo.backward(l)
                roo.write("Done By Pidugu Jatin")
        draw(60)



    def design_4(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)                                              # Pallavi Patel   2010DMTCSE07765
        t = tur
        t.pensize(2)
        t.speed(0)
        t.write("Done by Pallavi Patel ")
        while (True):
             for i in range(6):
                for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
                    t.color(colors)
                    t.circle(100)
                    t.left(10)
                t.hideturtle()


    def design_5(self):
        self.screen = turtle.TurtleScreen(self.c)                               #Nandani Verma   2010DMTCSE07762
        tur = turtle.RawTurtle(self.c)
        t = tur
        colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']
        t.speed(0)
        for x in range(200):
            t.pencolor(colors[x % 6])
            t.width(x / 100 + 1)
            t.forward(x)
            t.left(59)
        t.speed(10)
        for x in range(200):
            t.pencolor(colors[x % 6])
            t.width(x / 100 + 1)
            t.forward(x)
            t.left(59)
        t.write("Done by Nandani Verma ")


    def design_6(self):
        self.screen = turtle.TurtleScreen(self.c)            #Ayushi Anderiya  2010DMTCSE0
        tur = turtle.RawTurtle(self.c)
        t = tur
        t.pensize(2)
        t.speed(0)
        n = 36
        h = 0
        for i in range(89):
            c = colorsys.hsv_to_rgb(h, 1, 0.9)
            h += 1 / n
            t.pencolor(c)
            for j in range(5):
                t.forward(i - 3)
                t.right(9 * 5)
                t.left(8)
            t.right(115)
        t.write("Ayushi Anderiya  2010DMTCSE0")


    def design_8(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)
        colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]
        astroid = tur
        astroid.speed(0)
        for i in range(50):
            astroid.color(random.choice(colors))
            astroid.forward(i * 3)
            astroid.left(144)
        astroid.up()
        astroid.down()
        astroid.write("Astroid")
        astroid.hideturtle()

    def design_9(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)
        colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]
        triad = tur
        triad.speed(0)
        triad.up()
        triad.down()
        for i in range(50):
            triad.color(random.choice(colors))
            triad.forward(i * 3)
            triad.left(120)
            for i in range(50):
                triad.color(random.choice(colors))
                triad.forward(i * 3)
                triad.left(120)
        triad.up()
        triad.down()
        triad.write("Triad")
        triad.hideturtle()

    def design_10(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)
        colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]
        squad = tur
        squad.speed(0)
        squad.up()
        squad.down()
        for i in range(50):
            squad.color(random.choice(colors))
            squad.forward(i * 2)
            squad.left(90)
        squad.up()
        squad.down()
        squad.write("Squad")
        squad.hideturtle()

    def design_11(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)
        colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]
        pentago = tur
        pentago.speed(0)
        pentago.up()
        pentago.down()
        for i in range(50):
            pentago.color(random.choice(colors))
            pentago.forward(i * 2)
            pentago.left(72)
        pentago.up()
        pentago.write("Pentago")
        pentago.hideturtle()

    def design_12(self):
        self.screen = turtle.TurtleScreen(self.c)
        tur = turtle.RawTurtle(self.c)
        colors = ["red", "gold", "blue", "green", "white", "cyan", "pink"]
        octago = tur
        octago.speed(0)
        octago.up()
        octago.down()
        for i in range(75):
            octago.color(random.choice(colors))
            octago.forward(i)
            octago.left(60)
        octago.up()
        octago.down()
        octago.write("Cherry Lonare ")
        octago.hideturtle()

    def mandel_1(self):
        self.screen = turtle.TurtleScreen(self.c)                  #Anjili Jain  #2010DMTCSE07746
        tur = turtle.RawTurtle(self.c)
        t = tur
        t.color("#ffcc00")
        t.pensize(2)
        t.speed(0)
        def pen(x, y):
            t.penup()
            t.goto(x, y)
            t.pendown()
        def pattern():
            for i in range(23):
                t.forward(360)
                t.circle(20)
                t.left(216 + 3)
        def star():
            t.begin_fill()
            for i in range(9):
                t.forward(80)
                t.left(160)
            t.end_fill()
        pen(-200, 100)
        pattern()
        pen(-30, -184)
        t.circle(220)
        pen(-30, -194)
        t.circle(230)
        pen(-30, -144)
        t.circle(180)
        pen(-60, 30)
        star()
        pen(-21, -10)
        t.circle(46)
        t.hideturtle()

    def mandel_2(self):
        self.screen = turtle.TurtleScreen(self.c)                               # Done By Pidugu Jatin
        tur = turtle.RawTurtle(self.c)                                          # 21100BTCSE09917
        squary = tur
        squary.speed(0)
        for i in range(200):
            squary.forward(i)
            squary.left(91)
        squary.write("Done By Pidugu Jatin ")

    def mandel_3(self):
        self.screen = turtle.TurtleScreen(self.c)                              # Done By Pidugu Jatin
        tur = turtle.RawTurtle(self.c)
        ninja = tur
        ninja.speed(0)
        for i in range(180):
            ninja.forward(100)
            ninja.right(30)
            ninja.forward(20)
            ninja.left(60)
            ninja.forward(50)
            ninja.right(30)
            ninja.penup()
            ninja.setposition(0, 0)
            ninja.pendown()
            ninja.right(2)
        ninja.write("Pidugu Jatin")

    def mandel_4(self):
        self.screen = turtle.TurtleScreen(self.c)                              # Done By Pidugu Jatin
        tur = turtle.RawTurtle(self.c)
        painter = tur
        painter.pencolor("blue")
        for i in range(50):
            painter.forward(50)
            painter.left(123)
        painter.pencolor("red")
        for i in range(50):
            painter.forward(100)
            painter.left(123)
        painter.write("Pidugu Jatin")

    def mandel_5(self):
        self.screen = turtle.TurtleScreen(self.c)                              # Done By Pidugu Jatin
        tur = turtle.RawTurtle(self.c)
        s = tur
        r = 10
        for i in range(20):
            s.circle(r * i)
            s.penup()
            s.sety(r * i * -1)
            s.setx(r * i * -1)
            s.pendown()
            j = random.random()
            k = random.random()
            l = random.random()
            s.pencolor((j, k, l))
        s.penup()
        s.home()
        s.pendown()
        for i in range(20):
            s.circle(r * i)
            s.penup()
            s.setx(r * i)
            s.sety(r * i * -1)
            s.pendown()
            j = random.random()
            k = random.random()
            l = random.random()
            s.pencolor((j, k, l))
        s.hideturtle()

    def mandel_6(self):
        self.screen = turtle.TurtleScreen(self.c)                                     # Done By Pidugu Jatin
        tur = turtle.RawTurtle(self.c)                                                 # 21100BTCSE09917
        squary = tur
        squary.speed(0)
        for i in range(500):
            squary.forward(i)
            squary.left(91)


if __name__ == '__main__':
    Paint()