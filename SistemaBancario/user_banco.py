import re 
import os

usuarios = []

def main():

    while True:

        print('\n{:=^30}'.format(' BANCO DIO '))

        menu = """\n
[ 1 ] NOVO USUÁRIO
[ 2 ] NOVA CONTA
[ 3 ] PESQUISAR USUÁRIO
[ 4 ] SAIR

OPÇÃO: """
        
        
        opcao = input(f"{menu}")
        

        print('=' * 30)

        if opcao == '1':
            novo_usuario(usuarios)
        elif opcao == '2':
            criar_conta_corrente(usuarios)   
        elif opcao == '3':
            if not usuarios:
                print('\nNão tem nenhum usuario cadastrado ainda!!!')
                return main()
            else:
                dados_usuarios(usuarios)

        elif opcao == '4':
            print('\nVolte Sempre!!!')
            print('=' * 30)
            break

        else:
            print('Opção invalida...Tente novamente...')
            return main()
            
    
            
        

def novo_usuario(usuarios):
    
    while True:
        
        cpf = input('\nCPF: ')
        
        for usuario in usuarios:
            if cpf == usuario['cpf']:
                print('Já existe um usuario para este CPF!!!')
                perg = input('\nQuer tentar outro CPF? [S/N]: ').upper().strip()
                if perg == 'S':
                    print("Insira novamente o CPF...")
                elif perg == 'N':
                    break 
                else:
                    print('Opção invalida...Tente novamente...')
        break      
         
            
    while True:
        
        nome = input('\nNome: ').title()

        if nome == "":
            print('=' * 30)
            raise ValueError("\nNada foi digitado!!!")
    
        else:
            break
        
    while True:
        nasc = input('\nData de Nascimento (dd/mm/aaaa): ')
        
        if re.match(r'^\d{2}/\d{2}/\d{4}$', nasc):
            break
        else:
            print("Formato inválido. Por favor, insira a data de nascimento no formato dd/mm/aaaa.")
    while True:
        try:    
            
            endereco = {
                
                'logradouro': input('\nLogradouro: ').title().strip(),
                'numero': input('Nº: ').strip(),
                'bairro': input('Bairro: ').title().strip(),
                'cidade': input('Cidade: ').title().strip(),
                'estado': input('Estado (AB): ').upper().strip()
            }
            
            if any(value == "" for value in endereco.values()):
                print('=' * 30)
                raise ValueError("\nO endereço não foi inserido corretamente!!!")
        
            else:
                break
        except ValueError as ve:
                print(ve) 
            
    usuario = {
        'cpf': cpf,
        'nome': nome,
        'nasc': nasc,
        'endereco': endereco,
        'conta': []
    }

    usuarios.append(usuario)

    print('Usuario Cadastrado com Sucesso!!!')

    novo = input('Cadastrar mais um Usuario? [S/N]: ').upper().strip()

    if novo == 'S':
        return novo_usuario(usuarios)
    elif novo == 'N':
        main()
    else:
        print('Resposta Invalida...')
        

def dados_usuario(usuarios):

    cpf = input("CPF: ")

   
    print("\n{:=^30}".format(' USUÁRIO CADASTRADO '))
    for user in usuarios:
        if user['cpf'] == cpf:
            print(f"""
            Nome: {user['nome']}
            CPF: {user['cpf']}
            Data de nascimento: {user['nasc']}
            Rua: {user['endereco']['logradouro']}
            Nº: {user['endereco']['numero']}
            Bairro: {user['endereco']['bairro']}
            Cidade: {user['endereco']['cidade']}
            Estado: {user['endereco']['estado']}
            Contas: {user['conta']}
            """)
            print('=' * 30)
        else:
            print("Usuario não encontrado!!!")
    


    main()


def criar_conta_corrente(usuarios):
    
    qtd_contas = 0
    for usuario in usuarios:
        for conta in usuario['conta']:
            if int(conta) > qtd_contas:
                qtd_contas = conta
            

    num_conta = qtd_contas + 1
   

    cpf = input('\nCPF: ')
    for user in usuarios:
        if user['cpf'] == cpf:
            user['conta'].append(f"{num_conta[0]} Agência: 0001") 
            print("Conta adicionada com Sucesso!!!")
            break
    else:
        print("Usuário não encontrado.")
    
    main()

            
        
if __name__ == '__main__':
    main()