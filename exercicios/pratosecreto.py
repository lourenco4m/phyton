import random

def jogo_adivinhar_prato():
    # Lista de pratos deliciosos
    pratos = ["Pizza", "Lasanha", "Hamburguer", "Sushi", "Churrasco", "Salada", "Macarrão", "Taco"]
    
    # Escolha aleatória do prato secreto
    prato_secreto = random.choice(pratos)
    
    # Número de tentativas
    tentativas = 5
    
    print("Bem-vindo ao jogo de adivinhação de pratos!")
    print("Tente adivinhar qual é o prato secreto.")
    print(f"Você tem {tentativas} tentativas.\n")
    
    # Mostrar as opções para ajudar o jogador
    print("Lista de pratos possíveis:")
    for prato in pratos:
        print(f"- {prato}")
    
    # Loop de tentativas
    for tentativa in range(1, tentativas + 1):
        chute = input(f"\nTentativa {tentativa}: Digite o nome de um prato: ").strip()
        
        if chute.lower() == prato_secreto.lower():
            print(f"\nParabéns! Você acertou o prato secreto: {prato_secreto}!")
            break
        else:
            tentativas_restantes = tentativas - tentativa
            if tentativas_restantes > 0:
                print(f"Errado! Você ainda tem {tentativas_restantes} tentativa(s).")
            else:
                print(f"\nSuas tentativas acabaram. O prato secreto era: {prato_secreto}.")
                break

# Iniciar o jogo
jogo_adivinhar_prato()
