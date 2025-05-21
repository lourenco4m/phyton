import random

def escolher_dificuldade():
    print("Escolha o nível de dificuldade:")
    print("1 - Fácil (30 tentativas)")
    print("2 - Médio (15 tentativas)")
    print("3 - Difícil (5 tentativas)")

    while True:
        escolha = input("Digite a opção (1, 2 ou 3): ")
        if escolha == '1':
            return 'Fácil', 30, 10
        elif escolha == '2':
            return 'Médio', 15, 20
        elif escolha == '3':
            return 'Difícil', 5, 50
        else:
            print("Opção inválida! Tente novamente.")

def obter_numero_do_jogador():
    while True:
        try:
            numero = int(input("Digite um número entre 10 e 100: "))
            if 10 <= numero <= 100:
                return numero
            else:
                print("Número fora do intervalo! Tente novamente.")
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")

def jogar_numero_secreto():
    print("Bem-vindo ao Jogo do Número Secreto!")
    
    # Definindo o número secreto
    numero_secreto = random.randint(10, 100)

    # Escolhendo a dificuldade
    dificuldade, tentativas, perda_por_erro = escolher_dificuldade()

    # Pontuação inicial
    pontos = 100

    # Loop de tentativas
    while tentativas > 0:
        print(f"\nVocê tem {tentativas} tentativa(s) restante(s).")
        print(f"Sua pontuação atual: {pontos} ponto(s).")
        
        chute = obter_numero_do_jogador()

        if chute == numero_secreto:
            print(f"Parabéns! Você acertou o número secreto {numero_secreto}!")
            print(f"Sua pontuação final: {pontos} ponto(s).")
            break
        else:
            tentativas -= 1
            pontos -= perda_por_erro
            if pontos < 0:
                pontos = 0
            if chute < numero_secreto:
                print("O número secreto é maior.")
            else:
                print("O número secreto é menor.")

        if tentativas == 0:
            print(f"\nFim de jogo! O número secreto era {numero_secreto}.")
            print(f"Sua pontuação final: {pontos} ponto(s).")

if __name__ == "__main__":
    jogar_numero_secreto()
