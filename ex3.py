

def sum_to(n):

    """Inicializa a variável com soma zero"""
    sum = 0

    """A cada iteração, um termo da sequência é somado"""
    for i in range(1, n+1):
        sum += i
    
    """Printa no terminal a saída do resultado"""
    print('A soma de 1 até ' + str(n) + ' é ' + str(sum))

    """Retorna a soma final"""
    return sum


soma = sum_to(10)
print(soma)