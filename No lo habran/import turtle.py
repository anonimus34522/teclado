import turtle
import random

# Configuración de la pantalla
wn = turtle.Screen()
wn.title("Puntos y Puntaje")
wn.bgcolor("white")
wn.setup(width=800, height=600)

# Crear el punto verde que sigue al mouse
player = turtle.Turtle()
player.shape("circle")
player.color("green")
player.penup()

# Lista para almacenar los puntos rojos
red_points = []

# Crear el punto azul
blue_point = turtle.Turtle()
blue_point.shape("circle")
blue_point.color("blue")
blue_point.penup()
blue_point.shapesize(random.uniform(0.5, 2.0))  # Tamaño aleatorio
blue_point.goto(random.randint(-390, 390), random.randint(-290, 290))

# Configuración del puntaje
score = 0
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("black")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Puntaje: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Función para actualizar el puntaje en pantalla
def update_score():
    score_display.clear()
    score_display.write("Puntaje: {}".format(score), align="center", font=("Courier", 24, "normal"))

# Función para crear un nuevo punto rojo en una posición aleatoria
def create_red_point():
    red_point = turtle.Turtle()
    red_point.shape("circle")
    red_point.color("red")
    red_point.penup()
    red_point.shapesize(random.uniform(0.5, 2.0))  # Tamaño aleatorio
    red_point.goto(random.randint(-390, 390), random.randint(-290, 290))
    red_points.append(red_point)

# Crear el primer punto rojo
create_red_point()

# Función para mover el punto verde con el mouse
def move(x, y):
    player.setx(x)
    player.sety(y)

# Función para comprobar colisiones y actualizar el puntaje
def check_collision(x, y):
    global score
    for red_point in red_points:
        if player.distance(red_point) < 20:
            score += 10
            red_point.goto(random.randint(-390, 390), random.randint(-290, 290))
            red_point.shapesize(random.uniform(0.5, 2.0))  # Cambia el tamaño de forma aleatoria
            if score % 100 == 0:
                create_red_point()

    if player.distance(blue_point) < 20:
        score -= 10
        blue_point.goto(random.randint(-390, 390), random.randint(-290, 290))
        blue_point.shapesize(random.uniform(0.5, 2.0))  # Cambia el tamaño de forma aleatoria

    update_score()

# Vincular el movimiento del punto verde al movimiento del mouse
wn.listen()
wn.tracer(0)  # Apaga la actualización automática de la pantalla

# Vincular el clic izquierdo del mouse para actualizar el puntaje
wn.onscreenclick(check_collision, btn=1)

# Bucle principal del juego
while True:
    wn.update()  # Actualiza la pantalla manualmente
    x, y = wn.cv.winfo_pointerx() - wn.cv.winfo_rootx(), wn.cv.winfo_pointery() - wn.cv.winfo_rooty()
    move(x - 400, 300 - y)  # Ajusta las coordenadas del mouse al sistema de coordenadas de turtle