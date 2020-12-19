#Criando a variável que acomodará a quantidade de números que atende aos requisitos
total = 0

#Criando lista que armazenará os valores que atende aos requisitos
minhaLista = []

for i in range(0, 5000000):

    #Verificando os requisitos e acomodando a quantidade de numeros que os atende
    if (i%2 == 0) and (i%37 == 0) and (i%49 == 0):
        minhaLista.append(i)
        total = total + 1

#Resposta
print("A quantidade de números entre 1 e 5000000 que satisfaz as exigências é {}.".format(total))

#Lista com todos os números que atendem aos requisitos
print(minhaLista)
