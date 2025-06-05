Lista1 = ['Frango', 'arroz', 'macarrao' ]
print( 90 * '-')
print('Mostrando index da lista')
print(Lista1.index('macarrao'))
print( 90 * '-')

print('Verificando se ha na lista')
print('carne suina' in Lista1)
print('macarrao' in Lista1)

print( 90 * '-')
print('Somando duas listas')
Lista2 = ['Sorvete', 'bolacha', 'lanche', 'batata']

ListaCompleta = Lista1 + Lista2

print(ListaCompleta)
print( 90 * '-')
print('Mostrando itens na ordem')
for i in range(2,5):
    print(ListaCompleta[i])

print( 90 * '-')
print('Repetindo a lista')
ListaRep = Lista1*3
print(ListaRep)

print( 90 * '-')
print('soma')

ListaNumeros = [1,2,3,4,5,6,7,8,9,10]
print(sum(ListaNumeros))

print( 90 * '-')
print('Maior e menor')

print(min(ListaNumeros))
print(max(ListaNumeros))

print( 90 * '-')
print('Tamanho')

print(len(ListaNumeros))

print( 90 * '-')
print('Primeiro e ultimo')

print('primeiro item da lista ', Lista1[0])
print('ultimo item da lista ', Lista1[-1])

print( 90 * '-')
print('Ordem Decrescente')

ListaNumeros.sort(reverse=True)

print(ListaNumeros)

print( 90 * '-')
print('Inserindo Valor')

minhaLista = []
minhaLista.append(input('Digite um valor pra lista: '))
print(minhaLista)

print( 90 * '-')
print('Insirindo valores')

MinhaLista2 = []

print('Quantos valores voce quer adicionar a lista?')
resposta = (int(input()))

print('Insira ', resposta, ' valores')

for i in range(resposta):
    MinhaLista2.append(input())

print(MinhaLista2)

