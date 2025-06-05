print("Insira o tanto de numeros para o Fibonacci")
Sequencia = int(input())

numeroAnterior = 0
numeroAtual = 1
numeroFuturo = 0

if Sequencia == 0:
    print("Numero de sequecia nulo")

if Sequencia == 1:
    print(numeroAnterior)

elif Sequencia == 2:
    print(numeroAnterior, numeroAtual)

else:
    print(numeroAnterior)
    print(numeroAtual)
    for numeroFuturo in range(Sequencia - 2):
        numeroFuturo = numeroAnterior + numeroAtual
        numeroAnterior = numeroAtual
        numeroAtual = numeroFuturo
        print(numeroFuturo)