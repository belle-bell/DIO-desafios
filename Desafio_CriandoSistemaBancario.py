# Desafio de Projeto - Criando um Sitema Bancário com Python 

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

-> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3


def realizar_deposito():
    valor = float(input("Informe o valor do depósito: "))
    if valor > 0:
        return valor
    print("Operação falhou! O valor informado é inválido.")
    return 0

def realizar_saque():
    valor = float(input("Informe o valor do saque: "))
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
        return 0
    if valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
        return 0
    if numero_saques >= LIMITE_SAQUES:
        print("Operação falhou! Número máximo de saques excedido.")
        return 0
    if valor > 0:
        return valor
    print("Operação falhou! O valor informado é inválido.")
    return 0

def exibir_extrato():
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

while True:
    opcao = input(menu)

    if opcao == "d":
        deposito = realizar_deposito()
        saldo += deposito
        if deposito > 0:
            extrato += f"Depósito: R$ {deposito:.2f}\n"

    elif opcao == "s":
        saque = realizar_saque()
        if saque > 0:
            saldo -= saque
            extrato += f"Saque: R$ {saque:.2f}\n"
            numero_saques += 1

    elif opcao == "e":
        exibir_extrato()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")