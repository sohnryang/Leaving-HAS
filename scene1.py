import turtle
from primary.displayLicense import *
from time import time
from math import *
import vlc


def standBy(screen, brush):
    """
    음원 저작권을 표시하는 함수입니다.

    :param screen: 저작권을 표시할 화면
    :param brush: 저작권을 표시할 때 사용할 turtle
    :return: Null
    """
    brush.clear()
    screen.bgcolor("#000000")
    width = screen.window_width()
    height = screen.window_height()
    brush.pu()
    brush.goto(width / 2, height)
    brush.color("#ffffff", "#ffffff")

    bgmLicense(screen, brush, "On the hill(Organ.ver)", "임샛별", \
               "공유마당 저작권 위원회 (https://gongu.copyright.or.kr/)", "CC BY")
    brush.clear()


def loadBGM():
    """
    배경음악을 불러오는 함수입니다.

    :return: 박 사이 간격 (초 단위, 리스트), 배경 음악 (vlc MediaPlayer), 현재 시간
    """
    bgm = vlc.MediaPlayer("bgm/온_더_힐_오르간_버전(On_the_hill_Organ_ver.)/LP1607110010_임샛별_On the hill (Organ ver.).mp3")
    schedule = []
    with open("bgm/drums.txt", 'r') as f:
        raw = f.read().split("\n")
    for r in range(len(raw)):
        try:
            if r == 0:
                schedule.append(float(raw[r]))
            else:
                schedule.append(float(raw[r]) - float(raw[r - 1]))
        except ValueError:
            pass

    return schedule, bgm, time()


def roulette(screen: turtle.TurtleScreen, brush: turtle.Turtle, color: str,
             center: list, radius: float, partitions: list, font: tuple, theta0: float):
    """
    화면에 룰렛을 그리는 함수입니다.

    :param screen: 룰렛을 그릴 화면
    :param brush: 룰렛을 그릴 turtle
    :param color: 룰렛의 색깔
    :param center: 룰렛의 중심 좌표
    :param radius: 룰렛의 반지름
    :param partitions: 룰렛의 구성 항목들
    :param font: 룰렛 항목의 폰트
    :param theta0: 룰렛의 초기각
    :return: None
    """

    # 상수
    CRUST = 0.05 # 룰렛 테두리 폭의 룰렛 반지름에 대한 비

    # 초기 설정
    brush.color(color, color)
    brush.pu()
    brush.goto(center[0], center[1])
    brush.dot()
    brush.goto(center[0], center[1] - radius)

    # 테두리
    brush.begin_fill()
    brush.circle(radius)
    brush.end_fill()

    # 안쪽
    brush.goto(center[0], center[1] - radius + CRUST * radius)
    brush.color(color, screen.bgcolor())
    brush.begin_fill()
    brush.circle(radius - CRUST * radius)
    brush.end_fill()

    partitionsLength = len(partitions)
    unitAngle = 2 * pi * (1 / partitionsLength)

    # 항목 작성
    for partition in range(partitionsLength):
        brush.pu()
        brush.goto(center[0], center[1])
        partitionAngle = unitAngle * partition
        brush.pd()
        brush.goto(center[0] + (1 - CRUST) * radius * cos(theta0 + partitionAngle),
                   center[1] + (1 - CRUST) * radius * sin(theta0 + partitionAngle))
        brush.pu()
        brush.goto(center[0] + 0.5 * (1 - CRUST) * radius * cos(theta0 + partitionAngle + 0.5 * unitAngle),
                   center[1] + 0.5 * (1 - CRUST) * radius * sin(theta0 + partitionAngle + 0.5 * unitAngle))
        brush.write(partitions[partition], False, "center", font)
        brush.pu()
        brush.goto(center[0] + (1 - CRUST) * radius * cos(theta0 + partitionAngle + unitAngle),
                   center[1] + (1 - CRUST) * radius * sin(theta0 + partitionAngle + unitAngle))
        brush.pd()
        brush.goto(center[0], center[1])


# TODO : 첫 씬은 작도하는 느낌으로 가는 것이 가장 좋을 듯. → 숫자 9 작도하기 (필요 개체 : 샤프, 자, 컴퍼스)



if __name__ == "__main__":
    brush = turtle.Turtle()
    screen = turtle.Screen()
    screen.setup(1024, 600, 100, 100)
    screen.setworldcoordinates(0, 0, 1024, 600)
    screen.tracer(0, 0)
    screen.bgcolor("#000000")
    roulette(screen, brush, "#ffffff", [512, 300], 200, ['가', '나', '다'], ("부산체_가칭", 40, "normal"), pi/5)
    screen.exitonclick()
    #: utf-16 필요한데 utf-8로 열음
