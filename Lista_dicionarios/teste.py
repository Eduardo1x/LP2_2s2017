dic_vazio = {}

alunos = {11111: "Alberto", 22222: "Bruna"}
aluno = {"nome": "Alberto", "idade": 26}
agenda = {"Igor": "555-555", "Jorge": "555-666"}

print(alunos[11111])
print(aluno['idade'])

alunos[11111] = 'Amanda'
aluno['idade'] = 20
agenda['Jorge'] = "555-000"

alunos[33333] = 'Carlos'
aluno['sexo'] = "M"
agenda['Marcos'] = "666-666"

print(alunos)
print(aluno)
print(agenda)

tamAlunos = len(alunos)
tamAluno = len(aluno)
tamAgenda = len(agenda)

print(tamAlunos, tamAluno, tamAgenda)


del agenda["Igor"]
print(agenda)

existe = "Marcos" in agenda
print(existe)
existe = "Igor" in agenda
print(existe)

chaves = alunos.keys()
print(chaves)
valores = alunos.values()
print(valores)
items = alunos.items()
print(items)

for chave, valor in alunos.items():
    print(chave)
    print(valor)

item = alunos.get(4444, "Não existe")
print(item)


aluno.clear()
print(aluno)


