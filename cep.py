import requests

#cep =input('Digite o cep')

#link = f"http://viacep.com.br/ws/{cep}/json/"

#requisicao = requests.get(link)
#dicRequisicao = requisicao.json()
#print(dicRequisicao)


#print(dicRequisicao['uf'])

print(120*"--")

link2 = f"https://economia.awesomeapi.com.br/last/USD-BRL"
requisicao = requests.get(link2)
dolarRequisição = requisicao.json()
dicRequisicao = requisicao.json()
print(dicRequisicao)
print("dolar para real hoje " +dolarRequisição['USDBRL']['high'])


