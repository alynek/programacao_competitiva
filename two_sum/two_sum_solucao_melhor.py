def two_sum(numeros, k):

    if len(numeros) > 1: 
                                                      
        dictionary = {}                                
        
        for indice, elemento in enumerate(numeros):    #1, 3, 7, 9, 2


            if elemento in dictionary:                  
                return [dictionary[elemento], indice]
            
            numeroAEncontrar = k - numeros[indice]      #24, 22, 18, 16, 23
            dictionary[numeroAEncontrar] = indice        #{ 24:0, 22:1, 18:2, 16:3, 23: 4}

    return None

print(two_sum([1, 3, 7, 9, 2], 11))   #saída esperada: [3 4]
print(two_sum([1, 3, 7, 9, 2], 8))   #saída esperada: [0 2]
print(two_sum([1, 3, 7, 9, 2], 10))   #saída esperada: [1 2]
print(two_sum([1, 3, 7, 9, 2], 3))   #saída esperada: [0 4]
print(two_sum([1, 3, 7, 9, 2], 12))   #saída esperada: [1 3]
print(two_sum([1, 3, 7, 9, 2], 25))    #saída esperada: None
print(two_sum([5], 25))                #saída esperada: None 
print(two_sum([], 25))                 #saída esperada: None 

#complexidade de tempo: O(n), sendo n o tamanho da lista
#complexidade  de espaço: O(1), isso porque não temos a criação de nenhuma variável que escala
