class Tabuada:
    def __init__(self, numero):
        self.numero = numero  # Atributo público
        self.__resultado = []  # Atributo privado

    def soma(self):
        print(f"\nTabuada de Soma do {self.numero}")
        self.__resultado = []
        for i in range(1, 11):
            resultado = self.numero + i
            self.__resultado.append(resultado)
            print(f"{self.numero} + {i} = {resultado}")

    def subtracao(self):
        print(f"\nTabuada de Subtração do {self.numero}")
        self.__resultado = []
        for i in range(1, 11):
            resultado = self.numero - i
            self.__resultado.append(resultado)
            print(f"{self.numero} - {i} = {resultado}")

    def multiplicacao(self):
        print(f"\nTabuada de Multiplicação do {self.numero}")
        self.__resultado = []
        for i in range(1, 11):
            resultado = self.numero * i
            self.__resultado.append(resultado)
            print(f"{self.numero} x {i} = {resultado}")

    def divisao(self):
        print(f"\nTabuada de Divisão do {self.numero}")
        self.__resultado = []
        for i in range(1, 11):
            resultado = self.numero / i
            self.__resultado.append(resultado)
            print(f"{self.numero} ÷ {i} = {resultado:.2f}")

# Programa principal (interativo)
def main():
    try:
        numero = int(input("Digite um número para ver a tabuada: "))
        tabuada = Tabuada(numero)

        tabuada.soma()
        tabuada.subtracao()
        tabuada.multiplicacao()
        tabuada.divisao()
    except ValueError:
        print("Por favor, digite um número inteiro válido.")

if __name__ == "__main__":
    main()
