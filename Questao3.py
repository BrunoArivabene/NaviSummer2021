#Criando a tupla
notas = {}

#Perguntando os dados aos usuários
i=1
while i <= 5:
    aluno = input(str("Insira o nome do aluno: "))
    nota = input("Insira a nota de {} no formato X.X: ".format(aluno))
    notas[aluno] = nota
    i= i + 1

#Dicionário com os alunos e as respectivas notas
print(notas)

#Resposta
maiornota = max(notas.values())
def search(term):
    for k, v in notas.items():
        if term in v:
            return k
alunomaiornota = search(maiornota)
print("A maior nota foi a de {}, que tirou {} pontos." .format(alunomaiornota,maiornota))


