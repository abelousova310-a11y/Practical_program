import turtle

# =====================================================
# КОНСТАНТЫ
# =====================================================
CLOUD_COLOR = "white"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 700
BG_COLOR = "lightblue"

STEAM_LENGTH = 120
PETAL_COUNT = 8
PETAL_RADIUS = 30
CENTRAL_RADIUS = 20
STEAM_WIDTH = 4
PETAL_COLOR = "pink"
CENTRAL_COLOR = "yellow"
STEAM_COLOR = "darkgreen"

GRASS_COLOR = "green"
BLADE_COUNT = 30  # увеличил для большего количества травы
BLADE_HEIGHT = 70
START_X = -350  # расширил зону травы
START_Y = -300
STEP_X = 20  # уменьшил шаг, чтобы травинки были чаще
ANGLE_BASE = 75
WIDTH_BASE = 3
ANGLE_STEP = 5
STEP_FORWARD = 10
MODULO_WIDTH = 2
MODULO_ANGLE = 30

# =====================================================
# НАСТРОЙКА ЭКРАНА
# =====================================================
t = turtle.Turtle()
t.speed(0)
t.hideturtle()
screen = turtle.Screen()
screen.bgcolor(BG_COLOR)
screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)


# =====================================================
# ФУНКЦИЯ 1 — СОЛНЫШКО (x, y — координаты ЦЕНТРА)
# =====================================================
def draw_sun(x, y):
    # Лучи
    t.color("orange")
    t.width(6)
    for i in range(16):
        t.penup()
        t.goto(x, y)  # центр солнца
        t.pendown()
        t.setheading(i * 22.5)
        t.forward(90)

    # Центр солнца
    t.width(1)
    t.penup()
    t.goto(x, y - 60)  # черепашка рисует круг от нижней точки
    t.pendown()
    t.color("yellow")
    t.begin_fill()
    t.circle(60)
    t.end_fill()


# =====================================================
# ФУНКЦИЯ 2 — ОБЛАКО (x, y — координаты НИЖНЕЙ ЦЕНТРАЛЬНОЙ точки)
# =====================================================
def draw_cloud(x, y):
    t.color(CLOUD_COLOR)

    coords = [
        (x, y, 40),
        (x - 30, y + 10, 30),
        (x + 30, y + 10, 30),
        (x - 50, y - 10, 25),
        (x + 50, y - 10, 25),
        (x, y - 20, 35)
    ]

    for cx, cy, radius in coords:
        t.penup()
        t.goto(cx, cy - radius)
        t.pendown()
        t.begin_fill()
        t.circle(radius)
        t.end_fill()


# =====================================================
# ФУНКЦИЯ 3 — ЦВЕТОК (x, y — координаты ОСНОВАНИЯ СТЕБЛЯ)
# =====================================================
def draw_flower(x, y):
    # Стебель
    t.color(STEAM_COLOR)
    t.width(STEAM_WIDTH)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.forward(STEAM_LENGTH)

    # Лепестки
    t.width(1)
    t.color(PETAL_COLOR)
    flower_center_x = x
    flower_center_y = y + STEAM_LENGTH

    for i in range(PETAL_COUNT):
        t.penup()
        t.goto(flower_center_x, flower_center_y)
        t.pendown()
        t.setheading(i * 45)
        t.begin_fill()
        t.circle(PETAL_RADIUS, 180)
        t.circle(PETAL_RADIUS, 180)
        t.end_fill()

    # Центр цветка
    t.penup()
    t.goto(flower_center_x, flower_center_y)
    t.pendown()
    t.color(CENTRAL_COLOR)
    t.begin_fill()
    t.circle(CENTRAL_RADIUS)
    t.end_fill()


# =====================================================
# ФУНКЦИЯ 4 — ТРАВА (x, y — координаты НИЖНЕЙ ЛЕВОЙ точки)
# =====================================================
def draw_grass(x, y):
    t.color(GRASS_COLOR)
    for i in range(BLADE_COUNT):
        t.penup()
        t.goto(x + i * STEP_X, y)
        t.pendown()
        d = 1 if i % 2 == 0 else -1
        t.setheading(ANGLE_BASE + (i % MODULO_ANGLE))
        t.width(WIDTH_BASE - (i % MODULO_WIDTH))
        n = BLADE_HEIGHT + (i % 30)
        for j in range(int(n / STEP_FORWARD)):
            t.forward(STEP_FORWARD)
            t.left(ANGLE_STEP * d)
        t.width(1)


# =====================================================
# ТЕСТИРОВАНИЕ — вызов функций с конкретными координатами
# =====================================================
if __name__ == "__main__":
# Солнышко (центр) — исправлено, теперь рисуется по центру


    draw_sun(300, 250)

# 3 облака в разных местах
    draw_cloud(-200, 300)  # левое облако
    draw_cloud(100, 280)  # центральное облако
    draw_cloud(350, 310)  # правое облако

# 3 цветка
    draw_flower(-200, -300)  # левый цветок
    draw_flower(0, -300)  # центральный цветок
    draw_flower(200, -300)  # правый цветок

# Трава — больше и шире
    draw_grass(-380, -300)

turtle.done()