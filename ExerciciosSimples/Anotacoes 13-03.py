##meuDicionario = {'chave1': valorChave1, 'chave2': valorChave1,'chave3': valorChave1,'chave4': valorChave1, }

meuDicionario = {'chave1': 30, 'chave2': 'Texto Puro','chave3': 5.1,'chave4': True }
valorChave2= meuDicionario.get('chave2')
print(valorChave2)
print(120*"-")

meuDicionario["chave5"] = 2023
meuDicionario["cahve06"] = False

print(meuDicionario)
print(120*"-")

dicionarioCores = {} #Criando um dicionario vazio

dicionarioCores['Green'] = 'Verde'
dicionarioCores['Black'] = 'Preto'
dicionarioCores['Red'] = 'Vermelho'
dicionarioCores['Blue'] = 'Azul'
#Apresentando valores, chave-valor individualmente

print(dicionarioCores)
print(120*"-")

novoDicionario = {}

for i in range(1,10):
    novoDicionario[i] = i*i

print(novoDicionario)

i=1

dicionario3={}

while i<5:
    dicionario3[i] = input('digite um adulto para ser adicionado nao usuario:')
    i+=1

print(dicionario3)

dicionarioCores = {}

dicionarioCores['Green'] = 'verde'
dicionarioCores['Black'] = 'Preto'
dicionarioCores['Red'] = 'Preto'
dicionarioCores['Blue'] = 'Azul'

print(dicionarioCores)

del dicionarioCores['Red']
print(dicionarioCores)





