def two_sum(numeros, k):

    if len(numeros) > 1:

        for p1 in range(len(numeros)):
            numeroAEncontrar = k - numeros[p1]
            for p2 in range(p1 + 1, len(numeros)):
                if numeroAEncontrar == numeros[p2]:
                    return [p1, p2]

    return None

two_sum([1, 3, 7, 9, 2], 11)  #saída esperada: 3 4  
two_sum([1, 3, 7, 9, 2], 25)  