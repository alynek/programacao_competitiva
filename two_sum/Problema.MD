Enunciado:
        Dado um array de números inteiros, retorne os índices dos dois números que somados, resultem em um certo k inteiro dado

Exemplo de dados de entrada:
        Array de inteiros: [1, 3, 7, 9, 2]
        k = 11

        Nesse exemplo, temos que 9 + 2 = 11, 
        então a saída esperada é: [3, 4] 
        sendo 3 e 4 os índices dos elemetnos do array 9 e 2 respectivamente

Analisando as constraints:
        Verificar quais são as constraints do problema, ou seja, descobrir as restrições que o problema tem, vamos fazer algumas perguntas...

        1 - Vai ser dada uma lista de inteiros, então estamos lidando com números negativos e positivos? 
                não, serão apenas números inteiros positivos 

        2 - No array vai ter números repetidos?
                não, serão sempre números distintos

        3 - Vai existir apenas 1 par de números no array, que resultará no tal número k, ou seja,  vamos ter apenas 1 solução?
                sim, vai ter apenas 1 par de números, ou seja, apenas 1 par de números vai ser solução como resposta

                ou seja, algo da forma: [x, y], sendo x e y, os índices resultantes

        4 - Sempre vai ter solução?
                não, podem existir casos de não termos solução alguma, 
        
                exemplo 1:
                        [1, 3, 7, 9, 2]
                        k = 25
                        sem solução, pois é impossível um certo x + y pertencente ao array fornecido que seja igual a 25

                exemplo 2:
                        []
                        k = 25 
                        sem solução, pois o array está vazio

                exemplo 3:
                        [5]
                        k = 5  
                        sem solução, pois perceba que mesmo que no array contenha o elemento 5, que é o nosso k, como temos apenas um elemento no array e não dois, isso ainda não é solução

        5 - O que retornar quando não existir solução?
                deve retornar null

Raciocinando:

        Temos um array , numeros = [1, 3, 7, 9, 2] e  k = 11

        podemos testar todas as possibilidades, no caso, podemos ter p1 e p2, sendo ponteiros se movendo no nosso array

                        (1, 3) (1, 7) (1, 9) (1, 2)     aqui p1 = 0, e p2 vai iterando pelos elementos até chegar no final do array
                        (3, 7) (3, 9) (3, 2)    aqui p1 = 1, e p2 vai iterando pelos elementos + 1 até chegar no final do array
                        (7, 9) (7, 2)   aqui p1 = 2, e p2 vai iterando pelos elementos + 2 até chegar no final do array
                        (9, 2)  BINGO!!


        Lembrando de teoria dos números...
        Se temos dois números a + b = c, temos que:
                a + b = c   <=>   a = c - b   <=>   b = c - a

        exemplo:
        11 = 9 + 2   <=>   11 - 9 = 2    <=>   11 - 2 = 9

        então podemos fazer algo como:

        numeroAEncontrar = k - array[p1]

        que??

        k - array[p1] , é k subtraído de array[p1] que conhecemos, resultando em p2 (que vai ser um número diferente a cada iteração)


        





