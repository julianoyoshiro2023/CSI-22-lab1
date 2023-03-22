import turtle


""" Exercício 2 """
def draw_poly(tartaruga, n, size):

    wn = turtle.Screen()

    """ Configura o tamanho e a cor da caneta """
    tartaruga.pen(fillcolor="black", pencolor="pink", pensize=3, pendown = False)
    tartaruga.speed(0)
    """ Inicializa a posição no canto inferior esquerdo """
    tartaruga.setposition(-size, -size)

    tartaruga.pendown()

    """ Desenha cada lado do polígono. Depois, a tartaruga rotaciona 360/n graus (ângulo externo) """
    for i in range(n):
        tartaruga.forward(size)
        tartaruga.left(360/n)

    wn.mainloop()


alex = turtle.Turtle()
draw_poly(alex, 12, 120)