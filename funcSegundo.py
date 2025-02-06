print("insira um valor de X napar função X^2+5")

X= int(input())

def simples (X):
    funcao = X * X + 5
    return (funcao)

def medio():
    resolucao = (simples(X)-5)/X
    return(resolucao)


print(simples(X))
print(medio())