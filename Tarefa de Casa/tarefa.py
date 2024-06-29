from datetime import datetime

def main():

    tarefas = []

    opcao = menu()
    
    while True:
        
        if opcao == '1':
            add_tarefa(tarefas)
            
        elif opcao == '2':
            consultar_tarefas(tarefas)
            
        elif opcao == '3':
            listar_tarefas(tarefas)

# Função para exibir data e hora atuais
def exibir_data_hora_atual():
    agora = datetime.now()
    data_hora_formatada = agora.strftime("%d-%m-%Y %H:%M:%S")
    print(f'\r{data_hora_formatada}', end='', flush=True)
    nome = input("\nDigite seu nome: ").title().strip()
    print("=" * 30)
    print(f'Olá {nome}, o que deseja fazer?')

    return nome



def menu():

    

    while True:
        # Exibir data e hora atual
        nome = exibir_data_hora_atual()

        # Exibir menu e obter opção do usuário
        menu = f"""
{"=" * 30} 

Olá {nome}, o que deseja fazer?

[ 1 ] Criar Tarefa
[ 2 ] Consultar Tarefa
[ 3 ] Listar Tarefas
[ 4 ] Deletar Tarefa
[ 5 ] Verificar Tarefas Pendentes do Dia 

Opção: """
        
        opcao = input(menu)

        return opcao
        

def add_tarefa(tarefas):

   

    while True:
        adicionar_tarefa = input("Tarefa: ").title().strip()
        tarefas.append(adicionar_tarefa)
        print(f"{adicionar_tarefa} adicionada a lista de Tarefas!!!")
        formato = "%d-%m-%Y"
        horario = input("Data para efetuar a tarefa: (DD-MM-AAAA): ")
        data = datetime.strptime(horario, formato)
        if not horario:
            print("Erro na entrada de dados...")
        elif data == False:
            print("Por favor,digite no formato de data correto...")
        else:
            local = tarefas.index(adicionar_tarefa)
            tarefas[local] += f" - {horario}\n"
            
        perg = input("Quer adicionar mais alguma Tarefa? [S/N]: ").lower().strip()
        if perg == "n":
            break
        elif perg == "s":
            print("Adicione outra Tarefa...")
            add_tarefa(tarefas)
        else:
            print("Opção invalida....")
    
    listar_tarefas(tarefas)
    

def consultar_tarefas(tarefas):
    if not tarefas:
        print("Voce ainda não tem tarefas adicionadas.")
        
    else:
        for chave, valor in enumerate(tarefas, start=1):
            print(f"{chave} - {valor}")
        consulta = int(input("Qual tarefa você quer consultar? "))
        indice = consulta - 1
        if consulta > len(tarefas):
            print("Você não adicionou esta tarefa!!")
            
        elif consulta <= 0:
            print('Somente numeros positivos...') 
        else:
            print(f"{consulta} - {tarefas[indice]}")
            


def listar_tarefas(tarefas):
    for chave, valor in enumerate(tarefas, start=1):
        print(f"{chave} - {valor}")
        break



    # Implementação do menu continua abaixo...
    # Inclua o restante do seu código de gerenciamento de tarefas aqui

                




if __name__ == "__main__":
    main()