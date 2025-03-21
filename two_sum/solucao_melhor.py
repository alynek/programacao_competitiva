def two_sum(numeros, k):

    if len(numeros) > 1: 
                                                      
        dicionario_numeros = {}                                
        
        for indice, elemento in enumerate(numeros):  

            if elemento in dicionario_numeros:                  
                return [dicionario_numeros[elemento], indice]
            
            numero_para_encontrar = k - numeros[indice]     
            dicionario_numeros[numero_para_encontrar] = indice     

    return None

#complexidade de tempo: O(n), sendo n o tamanho da lista
#complexidade  de espaço: O(n), isso porque existe a possibilidade de precisarmos adicionar todos os n-ésimos elementos da nossa lista de n elementos
