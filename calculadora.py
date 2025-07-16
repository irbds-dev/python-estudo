# CALCULADORA SIMPLES VIA CLI PARA TREINAR FUNÇÕES

def soma(num1, num2):
    return num1 + num2


def subtracao(num1, num2):
    return num1 - num2


def multiplicacao(num1, num2):
    return num1 * num2


def divisao(num1, num2):
    if num2 == 0:
        return "Não é possivel dividir por zero"
    return num1 / num2


while True:
    print(" 1: soma\n 2: subtração\n 3: multiplicação\n 4: divisão")
    operacao = int(input("Escolha a operação: "))

    if operacao < 0 or operacao > 4:
        print("\n\nEssa operação não existe\n\n")
        continue

    num1 = int(input("Digite o primeiro numero: "))
    num2 = int(input("Digite o segundo numero: "))
    match operacao:
        case 1:
            print(soma(num1, num2))
        case 2:
            print(subtracao(num1, num2))
        case 3:
            print(multiplicacao(num1, num2))
        case 4:
            print(divisao(num1, num2))

    encerrar = input("Deseja realizar outra conta? (s/n) ").lower()

    if encerrar != 's':
        break
