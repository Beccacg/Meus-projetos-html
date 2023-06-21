"""
Rebeca Carvalho Goldoni - pt-br - utf-8 - 24/05/2023
aula_24_05.py

from collections import Counter


# Aplicando o counter sobre um interavel do tipo lista com strings

lista = ['Marcia','Marcia','Alice','Alice','Antonio','Antonio','Pedro','Pedro']
print(f'\nResultado: {Counter(lista)}')
print(f'\nO tipo do resultado é: {type(Counter(lista))}\n')


# Aplicando o Counter sobre um iterável do tipo lista com números
lista = [1,1,1,2,2,2,3,3,4,4,4,5,3,45,45,66,42,36,105.19,105.19]
print(f'\nResultado: {Counter(lista)}')
print(f'\nO tipo do resultado é: {type(Counter(lista))}\n')


# Aplicando Counter sobre uma string
frase = ('IFRO Campus Ariquemes')
print(f'\nResultado: {Counter(frase)}')
print(f'\nO tipo do resultado é:{type(Counter(frase))}\n')


# Tentando acessar chaves de um DefaultDict:
dicionario = {'disciplina':'Algoritmos e Logica da Programação'}
print(f'\nDicionario original:{dicionario}')
print(f'\nAcessando a chave discplina do dicionario: {dicionario["disciplina"]}')
print(f'\nAcessando a chave curso do dicionario: {dicionario["curso"]}')


# Criando um dicionário utilizando o modulo collections defaultdict e lambda
from collections import defaultdict

dicionario = defaultdict(lambda:'None')
print(f'\nO valor do dicionario é: {dicionario}')
dicionario['disciplina'] = 'Algoritmos e Logica da Programação'
print(f'\nO dicionario agora possui o elemento:{dicionario}')
print(f'\nAcessando a chave disciplina do dicionario:{dicionario["disciplina"]}')
print(f'\nAcessando a chave curso do dicionario:{dicionario["curso"]}\n')


# Igualdade de dicionários comuns:
nome_1 = {'Gustavo': 28,'Andre': 33,'João': 15,'Alice':9,'Lais':5}
nome_2 = {'Andre': 33,'João': 15,'Gustavo': 28,'Lais':5,'Alice':9}
print(f'\nos dicionarios nome_1 e nome_2 são iguais? {nome_1 == nome_2}\n')


# Dicionários OrderedDict:
from collections import OrderedDict

nome_1 = OrderedDict({'Gustavo': 28,'Andre': 33,'João': 15,'Alice':9,'Lais':5})
print(f'\nO dicionario nome_1 possui os elementos:{nome_1}')
print(f'\nO tipo dos dados do dicionario nome_1 é: {type(nome_1)}\n')

nome_2 = OrderedDict({'Andre': 33,'João': 15,'Gustavo': 28,'Lais':5,'Alice':9})
print(f'\nO dicionario nome_2 possui os elementos:{nome_2}')
print(f'\nO tipo dos dados do dicionario nome_2 é: {type(nome_2)}\n')
print(f'\nOs dicionarios nome_1 e nome_2 são iguais e estão na mesma ordem? {nome_1 == nome_2}')


# OrderedDict - metodo move_to_end():
from collections import OrderedDict

nome = OrderedDict({'Gustavo': 28,'Andre': 33,'João': 15,'Alice':9,'Lais':5})
print(f'\nO dicionario original é: {nome}')
nome.move_to_end('Andre')
print(f'\nO dicionario foi modificado: {nome}\n')
"""

#  OrderedDict - move_to_end( chave, last = False)
from collections import OrderedDict

nome = OrderedDict({'Gustavo': 28,'Andre': 33,'João': 15,'Alice':9,'Lais': 5})













