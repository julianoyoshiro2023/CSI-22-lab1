import turtle


""" Exercício 1 """
def draw_squares(tartaruga):

    """ Cria uma tela """
    wn = turtle.Screen()

    """ Configura o tamanho e a cor da caneta """
    tartaruga.pen(fillcolor="black", pencolor="pink", pensize=3, pendown = False)
    tartaruga.speed(0)

    """ Tamanho inicial do lado do quadrado """
    size = 20

    """ Cria os 5 quadrados """
    for i in range(5):

        """ Inicia a posição da tartaruga no canto inferior esquerdo de um quadrado
        pela metade do tamanho do lado para x e y.
        """
        tartaruga.setposition(-size/2, -size/2)
        tartaruga.pendown()

        """ Desenha um quadrado """
        for j in range(4):
            
            tartaruga.forward(size)
            tartaruga.left(90)
        
        tartaruga.penup()

        """ O tamanho aumenta em 20 após cada iteração """
        size += 20
    
    wn.mainloop()


alex = turtle.Turtle()
draw_squares(alex)