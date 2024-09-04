import pygame
import sys

# Inicializar pygame
pygame.init()

# Configuración de la pantalla
ancho, alto = 800, 200
pantalla = pygame.display.set_mode((ancho, alto))
pygame.display.set_caption('Teclado Musical')

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)

# Definir las teclas del teclado
teclas = {
    pygame.K_a: 'C',
    pygame.K_s: 'D',
    pygame.K_d: 'E',
    pygame.K_f: 'F',
    pygame.K_g: 'G',
    pygame.K_h: 'A',
    pygame.K_j: 'B',
    pygame.K_k: 'C2'
}

# Cargar sonidos
def cargar_sonidos():
    sonidos = {}
    for nota in teclas.values():
        sonidos[nota] = pygame.mixer.Sound(f'sounds/{nota}.wav')
    return sonidos

sonidos = cargar_sonidos()

# Función para dibujar el teclado
def dibujar_teclado():
    pantalla.fill(BLANCO)
    ancho_tecla = ancho // len(teclas)
    for i, tecla in enumerate(teclas):
        pygame.draw.rect(pantalla, NEGRO, (i * ancho_tecla, 0, ancho_tecla, alto))
        pygame.draw.line(pantalla, BLANCO, (i * ancho_tecla, 0), (i * ancho_tecla, alto), 1)
    pygame.display.flip()

# Ejecutar el bucle principal
dibujar_teclado()
reproduciendo = False
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if evento.type == pygame.KEYDOWN:
            if evento.key in teclas:
                nota = teclas[evento.key]
                sonidos[nota].play()
                reproduciendo = True
        
        if evento.type == pygame.KEYUP:
            if evento.key in teclas:
                sonido = sonidos[teclas[evento.key]]
                sonido.stop()
                reproduciendo = False

    pygame.display.update()
