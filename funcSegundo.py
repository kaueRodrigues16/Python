import math

print("insira um valor de X napar função X^2+5")

X= int(input())

print("Insira um valor para A")
A = int(input())

print("Insira um valor para B")
B = int(input())

print("Insira um valor para C")
C = int(input())

def simples (X):
    funcao = X * X + 5
    return (funcao)

def medio():
    resolucao = (simples(X)-5)/X
    return(resolucao)

def desenharEquacacao( A, B ,C ):
    if A < 0:
        a = " - " + str(-A)
    elif A > 0:
        a = str(A)
    if B > 0:
        b = " + " + str(B)
    elif B < 0:
        b = " - " + str(-B)
    if C > 0:
        c = " + " + str(C)
    elif C < 0:
        c = " - " + str(-C)

    desenhoDaFormula = " F(x) = " + a + "X^2 " + b + "X " + c
    return (desenhoDaFormula)

def Delta(A , B , C):

    print(desenharEquacacao(A, B, C ))
    Delta = B * B - 4 * A * C

    x1 = ((-B) + math.sqrt(Delta)) / 2 * A
    x2 = ((-B) - math.sqrt(Delta)) / 2 * A

    resultado = "Delta = ", Delta , " X1 = ", x1 , " X2 = ",x2
    return (resultado)


print(simples(X))
print(medio())
