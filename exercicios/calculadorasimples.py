
def somar(a, b):
    return a + b


def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b


def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero!"


def calculadora():

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    print("Escolha a operação:")
    print("+ para soma")
    print("- para subtração")
    print("* para multiplicação")
    print("/ para divisão")
    
    operacao = input("Digite a operação desejada: ")


    if operacao == '+':
        resultado = somar(num1, num2)
    elif operacao == '-':
        resultado = subtrair(num1, num2)
    elif operacao == '*':
        resultado = multiplicar(num1, num2)
    elif operacao == '/':
        resultado = dividir(num1, num2)
    else:
        resultado = "Operação inválida!"

  
    print("Resultado:", resultado)


calculadora()
