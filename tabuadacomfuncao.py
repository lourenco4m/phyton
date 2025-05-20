# Função que mostra a tabuada de 1 a 10 de um número fornecido
def mostrar_tabuada(numero):
    print(f"\nTabuada do {numero}:")
    print("-" * 20)
    for i in range(1, 11):
        resultado = numero * i
        print(f"{numero} x {i:2} = {resultado}")
    print("-" * 20)

# Solicita ao usuário um número inteiro
try:
    numero_usuario = int(input("Digite um número inteiro para ver sua tabuada: "))
    mostrar_tabuada(numero_usuario)
except ValueError:
    print("Por favor, digite um número inteiro válido.")
