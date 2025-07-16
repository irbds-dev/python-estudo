# ALGUMAS BRINCADEIRAS COM CONDICIONAIS

print("### CONDICIONAIS ###")
nome = 'Rafael'
idade = 15
frutas = ["maça", "banana", "uva", "morango", "laranja"]
nome_idade = {'Igor': 26, 'Rafael': 15}

if (idade % 3 == 0):
    print("Idade é divisivel por 3")

if idade % 2 != 0:
    print("Idade não é divisivel por 2")

if (idade >= 18):
    print("Maior de idade")
else:
    print("Menor de idade")

if nome == 'Rafael':
    print("nome do usuario:", nome)

print(nome_idade['Rafael'] == idade)


print('\n\n### LAÇOS ###')
for i in range(5):
    print(i)

# Percorrendo uma lista
for fruta in frutas:
    if fruta != 'maça':
        print(fruta)

contador = 0
while contador < 5:
    resultado = contador % 2
    resultado = bool(resultado)
    print(resultado)
    contador += 1

# Não existe 'do while' em python, para simular podemos fazer:
contador = 0
while True:
    if contador < len(frutas):
        print(frutas[contador])
    else:
        break

    next = input("Deseja imprmir o proximo item da lista? (s/n)").lower()

    contador += 1

    if next != 's':
        break
