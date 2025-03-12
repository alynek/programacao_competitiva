import pytest
import two_sum.solucao_melhor as solucao_melhor

@pytest.mark.parametrize(
        
    "numero_para_encontrar, retorno_esperado",
    [
        (11, [3, 4]), 
        (8, [0, 2]),   
        (3, [0 ,4]), 
        (25, None),     
    ]
)

def test_two_sum_deve_retornar_corretamente_quando_lista_populada(numero_para_encontrar, retorno_esperado):

    resultado = solucao_melhor.two_sum([1, 3, 7, 9, 2], numero_para_encontrar)

    assert resultado == retorno_esperado

def test_two_sum_deve_retornar_corretamente_quando_lista_com_apenas_um_elemento():

    numero_entrada = 25
    resultado = solucao_melhor.two_sum([5], numero_entrada)

    retorno_esperado = None

    assert resultado == retorno_esperado

def test_two_sum_deve_retornar_corretamente_quando_lista_vazia():

    numero_entrada = 25
    resultado = solucao_melhor.two_sum([], numero_entrada)

    retorno_esperado = None

    assert resultado == retorno_esperado
