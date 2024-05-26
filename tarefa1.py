# como fazer sem o append?
quantidadedealunos= int(input("Qual a quantidade de alunos que existem na turma?"))
a = []
for i in range(0, quantidadedealunos):
    b= input("nome ")
    a.append(b)
print(a)
  
# jeito do rodrigo

quantidadedealunos= int(input("Qual a quantidade de alunos que existem na turma?"))
a = []
for i in range(0, quantidadedealunos):
    b= input(" ")
    a.append(b)
print(a)

# jeito sem intervenção do rodrigo 
quantidadedealunos= int(input("Qual a quantidade de alunos que existem na turma?"))
a = []
for i in range(0, quantidadedealunos):
    b= input("aluno ")
    a = a + [b]

for aluno in a:
    print(aluno)
# concatenação de listas []


# jeito chatgpt
quantidadedealunos = int(input("Qual a quantidade de alunos que existem na turma? "))
a = [None] * quantidadedealunos  # Cria uma lista com o tamanho especificado

for i in range(quantidadedealunos):
    a[i] = input("nome ")

for nome in a:
    print(nome)
    