# Desafio: Gerenciador de Notas
# Crie um programa que permita aos usuários realizar operações básicas em uma lista de notas:

# Adicionar nota: Permita que o usuário adicione uma nova nota à lista.
# Remover nota: Permita que o usuário remova uma nota específica da lista.
# Listar notas: Mostre todas as notas na lista.
# Média das notas: Calcule e exiba a média das notas presentes na lista.
# Sair: Encerre o programa.
# Utilize métodos como append(), remove(), sort() e index() para manipular a lista de notas.
import os

def main():


    menu = """===== Gerenciador de Notas =====

    1. Adicionar Nota
    2. Remover Nota
    3. Media das Notas
    4. Listar Notas
    5. Sair

Escolha uma opção: """

    return func_menu(menu)

def func_menu(menu):
    notas = []
    
    
    
    while True:
       
        try:

            opcao = int(input(menu))
            if opcao == 1:
                add_nota = float(input("Nota: "))
                notas.append(add_nota)
                print(f'Nota: {add_nota} adicionada a lista de Notas.')
            elif opcao == 2:
                for indice,nota in enumerate(notas, start=1):
                    print(f'{indice} - Nota: {nota}')
                    
                remover_nota = int(input("Qual nota irá remover? "))
                notas.pop(remover_nota - 1)
            elif opcao == 3:
                for nota in notas:
                    somar = sum(notas)
                    media = somar / len(notas)
                print(f"Média : {media:.1f}")
            elif opcao == 4:
                for indice,nota in enumerate(notas, start=1):
                    print(f'{indice} - Nota: {nota}')
            elif opcao == 5:
                print("Volte Sempre!!")
                break
            
            else:
                print("Opção Invalida..")
            
            
        except ValueError:
            print("Opção Invalida....")
    
        input()
        os.system("clear")        
        


if __name__ == "__main__":
    main()
            