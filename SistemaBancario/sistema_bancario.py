def menu():
    menu = """

[ D ] Depositar
[ S ] Sacar
[ E ] Extrato
[ Q ] Sair

=> """

    return input(menu).upper().strip()

def main():
    


    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3

    while True:

        opcao = menu()
        
        if opcao == "D":
            valor = float(input("Informe o valor do depósito: R$ "))

            saldo , extrato = depositar(saldo, valor, extrato)

        elif opcao == "S":

            valor = float(input("Informe o valor do saque: R$ "))
            
            saldo, extrato , numero_saques = saque(
                
                limite=limite,
                extrato=extrato,
                valor=valor,
                saldo=saldo,
                limite_saques=LIMITE_SAQUES,
                numero_saques=numero_saques
            )

        elif opcao == "E":
            func_extrato(saldo,extrato=extrato)
        elif opcao == "Q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato


def saque(*,limite, extrato, valor, saldo,limite_saques,numero_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo , extrato , numero_saques 


def func_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

main()