import primary.displayLicense as dl
from time import sleep
from math import *

def ccBumper(screen, brush, radius):
    #constants
    circRatio = 0.2
    fontRatio = 0.9
    textPosRatio = 0.72

    #code
    brush.clear()
    screen.bgcolor("#000000")
    brush.color("#ffffff", "#ffffff")
    width = screen.window_width()
    height = screen.window_height()
    i = 1
    terminal = degrees(width/(2*radius))
    turns = 2
    w = degrees((pi/6 + 2 * turns * pi)/terminal)
    t = 0
    while t <= terminal:
        theta = radians((w * t) % 360 + 60)
        dl.ccBy(brush, [width - radius * radians(1) * t, 3*height/5], radius, theta)
        screen.update()
        sleep(0.01)
        brush.clear()
        t += 2
    dl.ccBy(brush, [width - radius * radians(1) * t, 3*height/5], radius, pi/2)
    brush.goto(width/4, 3*height/5 - radius)
    brush.pensize(circRatio * radius)
    brush.pd()
    brush.circle(radius)
    brush.pu()
    brush.goto(width/4, 3*height/5 - textPosRatio * radius)
    brush.write("CC", move=False, align="center", font=('The Bold Font', int(fontRatio * radius), 'normal'))

    brush.goto(3*width/4, 3*height/5 - radius)
    brush.pensize(circRatio * radius)
    brush.pd()
    brush.circle(radius)
    brush.pu()
    brush.goto(3*width/4, 3*height/5 - textPosRatio * 1.3 * radius)
    brush.write("$", move=False, align="center", font=('The Bold Font', int(fontRatio * 1.3 * radius), 'normal'))
    brush.goto(3*width/4 + radius * cos(7*pi/10), 3*height/5 + radius * sin(7*pi/10))
    brush.pd()
    brush.goto(3*width/4 + radius * cos(17*pi/10), 3*height/5 + radius * sin(17*pi/10))
    brush.pu()
    
    brush.goto(width/2, 7*height/20)
    brush.write("이 프로그램은 크리에이티브 커먼즈 [저작권 표시 대한민국 라이선스]에 따라 이용할 수 있습니다.",\
                move=False, align="center", font=("부산체_가칭", 12, 'normal'))
    brush.goto(width/2, 6*height/20)
    brush.write("https://creativecommons.org/licenses/by-nc/4.0/deed.ko",\
                move=False, align="center", font=("부산체_가칭", 12, 'normal'))
    screen.update()
    
if __name__ == "__main__":
    import turtle as t
    screen = t.Screen()
    screen.setup(1024, 600, 100, 100)
    screen.setworldcoordinates(0, 0, 1024, 600)
    screen.tracer(0, 0)
    brush = t.Turtle()
    brush.ht()
    brush.pu()
    ccBumper(screen, brush, 80)
