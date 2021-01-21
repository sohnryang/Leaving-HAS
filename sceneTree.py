import scene0
import scene1
from time import sleep
import turtle as t

screen = t.Screen()
screen.setup(960, 540, 100, 100)
screen.setworldcoordinates(0, 0, 960, 540)
screen.tracer(0, 0)
brush = t.Turtle()
brush.ht()
brush.pu()

# Scene 0 : CC Bumper 띄우기
scene0.ccBumper(screen, brush, 80)
sleep(2)
scene1.standBy(screen, brush)
deltaSchedule, bgm, startTime = scene1.loadBGM()

# pop 명령어를 쉽게 사용하기 위해
deltaSchedule.reverse()

bgm.play()

# 4 번째 박부터 고려
sleep(deltaSchedule.pop() + deltaSchedule.pop() + deltaSchedule.pop() + deltaSchedule.pop())
screen.title("졸업")

screen.exitonclick()


