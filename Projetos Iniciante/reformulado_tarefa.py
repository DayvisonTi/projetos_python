import re

def main():

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    contas = []
    usuarios = []
    AGENCIA = '0001'
    LIMITE_SAQUES = 3

    
    while True:

        opcao = menu()

        if opcao == "d":

            valor = float(input("Informe o valor do depósito: R$"))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":

            valor = float(input("Informe o valor do saque: R$"))

            saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES = saque (
                
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES 
                )
        
        elif opcao == "e":
            mostrar_extrato(saldo, extrato)

        elif opcao == "nu":
            usuarios.append(novo_usuario(usuarios))

        elif opcao == "nc":
            num_conta = len(contas) + 1
            conta = nova_conta(usuarios,num_conta, AGENCIA)

            if conta:
                contas.append(conta)

        elif opcao == "pu":
            dados_usuario(usuarios)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def menu():

    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[pu] Pesquisar Usuário
[q] Sair

=> """

    opcao = input(menu)

    return opcao

def depositar(saldo, valor, extrato):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Deposito efetuado com Sucesso!!!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

def saque(saldo, valor, extrato, limite, numero_saques, limite_saques):

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
        print(f"Saque no valor de R${valor:.2f} efetuado com sucesso!!!")

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, valor, extrato, limite, numero_saques, limite_saques

def mostrar_extrato(saldo, extrato):
    
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

    return 

def novo_usuario(usuarios):

    while True:
        
        cpf = input('CPF: ')
        
        
        if any(usuario['cpf'] == cpf for usuario in usuarios):
            print('Já existe um usuario para este CPF!!!')
            perg = input('Quer tentar outro CPF? [S/N]: ').upper().strip()
            if perg == 'N':
                return
            
        else:
            break
       
            
    nome = input('Nome: ').title()

    nasc = input('Data de Nascimento (dd/mm/aaaa): ')
        
    endereco = {
                
        'logradouro': input('Logradouro: ').title().strip(),
        'numero': input('Nº: ').strip(),
        'bairro': input('Bairro: ').title().strip(),
        'cidade': input('Cidade: ').title().strip(),
        'estado': input('Estado (AB): ').upper().strip()
            }
    usuarios.append({'cpf': cpf,'nome': nome,'nasc': nasc,'endereco': endereco, 'conta': []})

    print('Usuario Cadastrado com Sucesso!!!')

    novo = input('Cadastrar mais um Usuario? [S/N]: ').upper().strip()

    if novo == 'S':
        return novo_usuario(usuarios)
    elif novo == 'N':
        return usuarios

    

def nova_conta(usuarios,num_conta, agencia):

    cpf = input('\nCPF: ')
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario['agencia'] = agencia
            usuario['conta'].append({'agencia':agencia, 'num_conta':num_conta})
            print(f"Conta criada para o usuário {usuario['nome']}.")
            return {'cpf': cpf, 'agencia': agencia, 'num_conta': num_conta}
            
        
    print("Necessário criar usuario!!!")
    return None
     


def dados_usuario(usuarios):

    cpf = input("CPF: ")

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("\n{:=^30}".format(' USUÁRIO CADASTRADO '))
            print(f"""
    Nome: {usuario['nome']}
    CPF: {usuario['cpf']}
    Data de nascimento: {usuario['nasc']}
    Endereço:
    Rua: {usuario['endereco']['logradouro']}
    Nº: {usuario['endereco']['numero']}
    Bairro: {usuario['endereco']['bairro']}
    Cidade: {usuario['endereco']['cidade']}
    Estado: {usuario['endereco']['estado']}
    Contas: {', '.join([f"Agência {conta['agencia']} Conta {conta['num_conta']}" for conta in usuario['conta']])}
""")
            print('=' * 30)
            return
        
    print("Usuario não encontrado!!!")


    
if __name__ == "__main__":
    main()