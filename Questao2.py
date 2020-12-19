from math import log

#Criando um vetor/lista
meuVetor = []

for i in range(1,11):

    #Calcularemos o fatorial para todos os "i's", independente se ele será utilizado na geração do valor ou não
    fat = 1
    j = 2
    while j <= i:
        fat = fat*j
        j = j+1

    #Verificando se o índice é par ou ímpar e gerando o seu respectivo valor
    if i%2 == 0:
        info = (3**i + 7*fat)
        meuVetor.append(info)
    elif i%2 != 0:
        info = (2**i + 4*log(i))
        meuVetor.append(info)

#Printando o vetor gerado
print(meuVetor)

#Resposta1
maiorvalor = max(meuVetor)
print("O maior valor presente no vetor solicitado é: {0:.2f}.".format(maiorvalor))

#Resposta2
media = sum(meuVetor)/len(meuVetor)
print ("A média dos componentes do vetor solicitado é: {0:.2f}.".format(media))

