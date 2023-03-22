import turtle


""" Exercício 4 """
def draw_spiral(tartaruga):

    """ Cria a tela """
    wn = turtle.Screen()

    """ Configura o tamanho e a cor da caneta """
    tartaruga.pen(fillcolor="black", pencolor="pink", pensize=2, pendown = False)
    tartaruga.speed(0)


    """ Define o tamanho do lado inicial e a posição inicial no canto inferior esquerdo"""
    size = 200
    tartaruga.setposition(-size/2 - 150, -size/2)
    tartaruga.pendown()

    """ 3 primeiros lados desenhados """
    for i in range(3):
        tartaruga.forward(size)
        tartaruga.left(90)

    
    """ A partir daqui, a cada dois lados desenhados, diminui o tamanho do lado em 4 unidades """
    for i in range(50):
        size -= 4

        for j in range(2):
            tartaruga.forward(size)
            tartaruga.left(90)
    
    tartaruga.penup()

    """ Inicializa a posição da tartaruga no canto direito e o lado com tamanho 200 """
    tartaruga.home()
    size = 200
    tartaruga.setposition(size/2 , -size/2)

    """Rotaciona a tartaruga levemente em 5 graus """
    tartaruga.pendown()
    tartaruga.left(5)

    """ 3 primeiros lados desenhados """
    for i in range(3):
        tartaruga.forward(size)
        tartaruga.left(90)

    """ A partir daqui, a cada dois lados desenhados, diminui o tamanho do lado em 4 unidades 
    e a rotação é de 89 graus e não de 90 """
    for i in range(50):

            size -= 4
            for j in range(2):
                tartaruga.forward(size)
                tartaruga.left(89)

    tartaruga.penup()
    wn.mainloop()
    

alex = turtle.Turtle()
draw_spiral(alex)