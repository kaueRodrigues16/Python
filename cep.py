import requests

#cep =input('Digite o cep')

#link = f"http://viacep.com.br/ws/{cep}/json/"

#requisicao = requests.get(link)
#dicRequisicao = requisicao.json()
#print(dicRequisicao)


#print(dicRequisicao['uf'])

print(120*"--")

dolar = f"https://economia.awesomeapi.com.br/last/USD-BRL"
peso = f"https://economia.awesomeapi.com.br/last/ARS-BRL"
BTC = f"https://economia.awesomeapi.com.br/last/BTC-BRL"
requisicaoDolar = requests.get(dolar)
requisicaoPeso = requests.get(peso)
requisicaoBTC = requests.get(BTC)
dolarRequisicao = requisicaoDolar.json()
pesoRequisicao = requisicaoPeso.json()
btcRequisicao = requisicaoBTC.json()

print("dolar para real hoje R$" +dolarRequisicao ['USDBRL']['high'])
print("o peso argentino para hoje: R$" +pesoRequisicao ['ARSBRL']['high'])
print("o bitcoin para hoje: R$" +btcRequisicao ['BTCBRL']['high'])

print(120*"--")

diaSemana = f"http://api.tempo.com/index.php?api_lang=br&localidad=12996&affiliate_id=tk99un15usak&v=3.0"

requisicaoSemana = requests.get(diaSemana)
requisicaoSemana = requisicaoSemana.json()
print(requisicaoSemana)
print('data: ', requisicaoSemana['day']['1']['date'])
print('dia: ',requisicaoSemana['day']['1']['name'])
print('tempo:', requisicaoSemana['day']['1']['symbol_description'])
print('temepratura minima: ',requisicaoSemana['day']['1']['tempmin'])
print('temepratura maxima: ',requisicaoSemana['day']['1']['tempmax'])
