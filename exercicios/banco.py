def criar_conta():
    titular = input("Digite o nome do titular da conta: ")
    
    while True:
        try:
            deposito_inicial = float(input("Digite o valor do depósito inicial: "))
            if deposito_inicial <= 0:
                print("O valor deve ser positivo.")
            else:
                break
        except ValueError:
            print("Por favor, digite um número válido.")
    
    conta = (titular,)  # Tupla para o nome
    saldo = [deposito_inicial]  # Lista para o saldo
    historico = [f"Depósito inicial: R$ {deposito_inicial:.2f}"]  # Lista para o histórico
    
    print(f"Conta criada com sucesso para {titular} com saldo de R$ {deposito_inicial:.2f}\n")
    return conta, saldo, historico

def depositar(saldo, historico):
    try:
        valor = float(input("Digite o valor a ser depositado: "))
        if valor <= 0:
            print("O valor do depósito deve ser positivo.")
        else:
            saldo[0] += valor
            historico.append(f"Depósito: R$ {valor:.2f}")
            print(f"Depósito realizado com sucesso. Saldo atual: R$ {saldo[0]:.2f}")
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

def sacar(saldo, historico):
    try:
        valor = float(input("Digite o valor a ser sacado: "))
        if valor <= 0:
            print("O valor do saque deve ser positivo.")
        elif valor > saldo[0]:
            print("Saldo insuficiente para realizar o saque.")
        else:
            saldo[0] -= valor
            historico.append(f"Saque: R$ {valor:.2f}")
            print(f"Saque realizado com sucesso. Saldo atual: R$ {saldo[0]:.2f}")
    except ValueError:
        print("Valor inválido. Por favor, digite um número.")

def consultar_saldo(saldo):
    print(f"Saldo atual: R$ {saldo[0]:.2f}")

def consultar_historico(historico):
    print("Histórico de transações:")
    for transacao in historico:
        print(f"- {transacao}")

def menu():
    print("\nMenu de opções:")
    print("1 - Depositar")
    print("2 - Sacar")
    print("3 - Consultar Saldo")
    print("4 - Consultar Histórico")
    print("5 - Sair")

def sistema_bancario():
    conta, saldo, historico = criar_conta()
    
    while True:
        menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            depositar(saldo, historico)
        elif opcao == '2':
            sacar(saldo, historico)
        elif opcao == '3':
            consultar_saldo(saldo)
        elif opcao == '4':
            consultar_historico(historico)
        elif opcao == '5':
            print("Encerrando o programa. Obrigado por usar o sistema bancário.")
            break
        else:
            print("Opção inválida. Tente novamente.")

# Iniciar o sistema bancário
sistema_bancario()
