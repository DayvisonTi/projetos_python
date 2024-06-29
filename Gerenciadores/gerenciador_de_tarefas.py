import os

from time import sleep


def menu():
    
    menu = """===== Gerenciador de Tarefas =====

    1. Adicionar tarefa
    2. Remover tarefa
    3. Marcar como concluída
    4. Listar tarefas
    5. Sair

Escolha uma opção: """

    return menu


def main():

    tarefas = []

    while True:

        limpar_terminal()

        try:
        
            opcao = int(input(menu()))
            
            if opcao == 1:
                
                tarefas = add_tarefa(tarefas)

            elif opcao == 2:
                remover_tarefa(tarefas)
                    
            elif opcao == 3:
                tarefa_concluida(tarefas)
                        
            elif opcao == 4:
                lista_tarefas(tarefas)
            
            elif opcao == 5:
                break
               
            else:
                print("Opção Invalida...")

    
        
        except ValueError:
            print("Entrada de dados errada....")


    print("Volte Sempre!!!")

    os.system("clear")

def add_tarefa(tarefas):
    
    while True:
        
        tarefa = input("Tarefa: ").title().strip()
        
        if not tarefa:
            print("Digite a tarefa corretamente...")
            add_tarefa(tarefas)
        
        else:
            tarefas.append(tarefa)
            print(f"Tarefa {tarefa} adicionada lista de Tarefas.")
            sleep(2)
        
        return tarefas

def remover_tarefa(tarefas):
    
    if not tarefas:
        print("Não tem nada na Lista de Tarefas!!!")
        sleep(2)
        return tarefas
    
    else:
        print(lista_tarefas(tarefas))
        remover = int(input("Qual tarefa irá remover? "))
        
        if remover <= 0 or remover > len(tarefas):
            print("Não existe esta tarefa na lista.")
            sleep(2)
        
        else:

            print(f"{remover} - {tarefas[remover - 1]} está Removida.2")
            tarefas.pop(remover - 1)
            sleep(2)
            
    return tarefas

def tarefa_concluida(tarefas):
    
    if not tarefas: 
        print("Não tem nada na Lista de Tarefas!!!")
        sleep(2)
    
    else:
        print(lista_tarefas(tarefas))
        concluida = int(input("Qual a Tarefa Concluida? "))

        if concluida <= 0 or concluida > len(tarefas):
            print("Não existe esta tarefa na lista.")
            sleep(2)
        
        else:
            print(f"{concluida} - {tarefas[concluida - 1]} - Concluida.")
            tarefas[concluida - 1] += " - Concluida"
            concluido = tarefas.pop(concluida - 1)
            tarefas.append(concluido)
            sleep(2)
            
    return tarefas

def lista_tarefas(tarefas):
    
    if not tarefas: 
        print("Não tem nada na Lista de Tarefas!!!")
        sleep(2)
    
    else:
        
        lista = [f"{indice} - {tarefa}" for indice, tarefa in enumerate(tarefas, start=1)]
        
        
        return "\n".join(lista)
        
    
def limpar_terminal():

    os.system("clear")
        

if __name__ == "__main__":
    main()