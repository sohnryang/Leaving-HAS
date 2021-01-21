from math import *
from time import *

def ccBy(brush, position, radius, rotation):
    #constants
    circRatio = 0.2
    headPosRatio = 0.55
    headCircRatio = 0.15
    neckLenRatio = 0.07
    shoulderWidthRatio = 0.53
    armLenRatio = 0.5
    armWidthRatio = 0.11
    legLenRatio = 0.55

    #code
    #outline
    brush.goto(position[0], position[1] - radius)
    brush.pensize(radius * circRatio)
    brush.pd()
    brush.circle(radius)
    brush.pu()

    #head
    brush.pensize(1)
    R = headPosRatio * radius
    brush.goto(position[0] + R * cos(rotation), position[1] + R * sin(rotation) - headCircRatio * radius)
    brush.pd()
    brush.begin_fill()
    brush.circle(headCircRatio * radius)
    brush.end_fill()

    #body - rectangles
    brush.pu()
    R = (headPosRatio - headCircRatio - neckLenRatio) * radius
    brush.goto(position[0] + R * cos(rotation), position[1] + R * sin(rotation))
    brush.begin_fill()
    brush.pd()

    R = (headPosRatio - headCircRatio - neckLenRatio) * radius
    r = (-3*shoulderWidthRatio/8) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - shoulderWidthRatio/8) * radius
    r = (-3*shoulderWidthRatio/8) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - shoulderWidthRatio/8) * radius
    r = (-shoulderWidthRatio/2) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - armLenRatio) * radius
    r = (-shoulderWidthRatio/2) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - armLenRatio) * radius
    r = (-shoulderWidthRatio/2 + armWidthRatio) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - armLenRatio - legLenRatio) * radius
    r = (-shoulderWidthRatio/2 + armWidthRatio) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - armLenRatio - legLenRatio) * radius
    r = (shoulderWidthRatio/2 - armWidthRatio) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - armLenRatio) * radius
    r = (shoulderWidthRatio/2 - armWidthRatio) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - armLenRatio) * radius
    r = (shoulderWidthRatio/2) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - shoulderWidthRatio/8) * radius
    r = (shoulderWidthRatio/2) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio - shoulderWidthRatio/8) * radius
    r = (3*shoulderWidthRatio/8) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio) * radius
    r = (3*shoulderWidthRatio/8) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2))

    R = (headPosRatio - headCircRatio - neckLenRatio) * radius
    brush.goto(position[0] + R * cos(rotation), position[1] + R * sin(rotation))
    brush.end_fill()
    brush.pu()
    
    #body - shoulder roundness
    #left shoulder
    R = (headPosRatio - headCircRatio - neckLenRatio - shoulderWidthRatio/8) * radius
    r = (-3*shoulderWidthRatio/8) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2) - (shoulderWidthRatio/8) * radius)
    brush.pd()
    brush.begin_fill()
    brush.circle((shoulderWidthRatio/8) * radius)
    brush.end_fill()
    brush.pu()
    #right shoulder
    R = (headPosRatio - headCircRatio - neckLenRatio - shoulderWidthRatio/8) * radius
    r = (3*shoulderWidthRatio/8) * radius
    brush.goto(position[0] + R * cos(rotation) + r * cos(rotation + pi/2), \
               position[1] + R * sin(rotation) + r * sin(rotation + pi/2) - (shoulderWidthRatio/8) * radius)
    brush.pd()
    brush.begin_fill()
    brush.circle((shoulderWidthRatio/8) * radius)
    brush.end_fill()
    brush.pu()
    
def bgmLicense(screen, brush, songTitle, author, source, lic):
    width = screen.window_width()
    height = screen.window_height()
    
    i = 1
    w = 6
    r = 30
    while i <= 703:
        theta = radians(i % 360 - 250)
        ccBy(brush, [width - r * radians(1) * i, height/12], r, theta)
        screen.update()
        sleep(0.01)
        brush.clear()
        i += w
    positionX = width - r * radians(1) * i

    brush.goto(positionX + 1.6 * r, height/10 + 12)
    brush.write(f"<{songTitle}>", move=False, align="left", font=("부산체_가칭", 15, "normal"))
    brush.goto(positionX + 1.6 * r, height/10 - 11)
    brush.write(f"by {author}", move=False, align="left", font=("부산체_가칭", 12, "normal"))
    brush.goto(positionX + 1.6 * r, height/10 - 34)
    brush.write(f"from {source}", move=False, align="left", \
                font=("부산체_가칭", 8, "normal"))
    brush.goto(positionX + 1.6 * r, height/10 - 46)
    brush.write(f'{author}의 "{songTitle}"은 {lic} 라이선스로 제공됩니다.', move=False, align="left", \
                font=("부산체_가칭", 7, "italic"))
    ccBy(brush, [positionX, height/12], r, pi/2)
    screen.update()
    sleep(2)

    brush.clear()
    i = 703
    w = 6
    r = 30
    while i >= -60:
        theta = radians(i % 360 - 250)
        ccBy(brush, [width - r * radians(1) * i, height/12], r, theta)
        screen.update()
        sleep(0.01)
        brush.clear()
        i -= w
    screen.update()

if __name__ == "__main__":
    from time import sleep
    import turtle as t
    brush = t.Turtle()
    screen = t.Screen()
    screen.setup(900, 600, 100, 100)
    screen.setworldcoordinates(0, 0, 900, 600)
    screen.tracer(0, 0)
    brush.ht()
    brush.pu()
    brush.color("#000000", "#000000")
    i = 1
    w = 3
    while i <= 390:
        theta = radians(i % 360 + 60)
        ccBy(brush, [900 - 100 * radians(1) * i, 300], 100, theta)
        screen.update()
        sleep(0.01)
        brush.clear()
        i += w
    ccBy(brush, [900 - 100 * radians(1) * i, 300], 100, pi/2)
    
