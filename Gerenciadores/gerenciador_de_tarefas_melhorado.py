import os
import re
from datetime import datetime
from pytz import timezone

def main():

    os.system("clear")

    tarefas = []

    fuso_horario = timezone("America/Sao_Paulo")

    hoje = datetime.now(fuso_horario)

    padrao_data = r'^\d{2}/\d{2}/\d{4}$'

    data_formatada = " {}/0{}/{} ".format(hoje.day,hoje.month,hoje.year)

    print("=" * 30)

    print("{:^30}".format("GERENCIADOR DE TAREFAS"))

    print("{:=^30}\n".format(data_formatada))

    nome = obter_nome_usuario()

    limpar_terminal()

    while True:
        try:
            opcao = menu(nome)

            limpar_terminal()

            if opcao == '1':
               criar_tarefas(tarefas, hoje, padrao_data)

            elif opcao == '2':
                consultar_tarefas(tarefas)

            elif opcao == '3':
                listar_tarefas(tarefas)
            elif opcao == '4':
             remover_tarefas(tarefas)
            elif opcao == '5':
              verificar_tarefas_pendentes(tarefas)
            elif opcao == '6':
                print("TENHA UM BOM DIA!!!")
                break
            else:
                print("OPÇÃO INVALIDA!!!!")
        except ValueError:
            print("ENTRADA DE DADOS ERRADA!!!")

    limpar_terminal()


def obter_nome_usuario():
    while True:
        nome = input("DIGITE SEU NOME: ").upper().strip()
        if not nome:
            print("VOCÊ NÃO DIGITOU NADA. TENTE NOVAMENTE.")
        elif nome.isdigit():
            print("NÚMEROS NÃO SÃO PERMITIDOS. DIGITE UM NOME VÁLIDO.")
        else:
            return nome


def menu(nome):

    while True:

        menu = f"""{"=" * 30} 
O QUE DESEJA FAZER {nome} ?
{"=" * 30} 

[ 1 ] CRIAR TAREFA
[ 2 ] CONSULTAR TAREFA
[ 3 ] LISTAR TAREFAS
[ 4 ] REMOVER TAREFAS
[ 5 ] VERIFICAR TAREFAS PENDENTES DO DIA
[ 6 ] SAIR

OPÇÃO: """
        opcao = input(menu)

        return opcao

def limpar_terminal():
    input()
    os.system("clear")

def criar_tarefas(tarefas, hoje, padrao_data):
    while True:
        print("=" * 30)
        add_tarefa = input("TAREFA: ").upper().strip()
        if not add_tarefa:
            print("VOCÊ NÃO ADICIONOU NENHUMA TAREFA.")
        else:
            while True:
                print("=" * 30)
                dia = input("AGENDAR TAREFA PARA QUE DIA? (DD/MM/AAAA): ").strip()
                if not dia:
                    print("VOCÊ NÃO ADICIONOU NENHUMA DATA!!!")
                else:
                    if re.match(padrao_data, dia):
                        data_objeto = datetime.strptime(dia, '%d/%m/%Y')
                        if data_objeto.date() < hoje.date():
                            print("ESSA DATA JÁ PASSOU!!!")
                        else:
                            tarefas.append({"tarefa":add_tarefa,"data":dia})
                            print(f"TAREFA {add_tarefa} ADICIONADA COM SUCESSO!!")
                            break

                    else:
                        print("A DATA ESTÁ INCORRETA,TENTE NOVAMENTE!!!")
            return tarefas


def consultar_tarefas(tarefas):
    while True:
        if tarefas:
            listar_tarefas(tarefas)
            consulta = int(input("QUAL TAREFA VOCÊ QUER CONSULTAR? Nº "))
            indice = consulta - 1
            print(f"TAREFA AGENDADA PARA {tarefas[indice]['data']}.")
        else:
            print("VOCÊ AINDA NÃO TEM TAREFAS PARA CONSULTAR!!!")
        return

def listar_tarefas(tarefas):
    if tarefas:
        for indice,tarefa in enumerate(tarefas, start=1):
            print(f"{indice} - {tarefa['tarefa']}")
    else:
        print("VOCÊ AINDA NÃO ADICIONOU TAREFAS!!!")

    return

def remover_tarefas(tarefas):
    if not tarefas:
        print("=" * 30)
        print("VOCÊ AINDA NÃO ADICIONOU TAREFAS!!!")
    else:
        for indice, tarefa in enumerate(tarefas, start=1):
                descricao = tarefa['tarefa']
                data = tarefa['data']
                print("=" * 30)
                print(f'{indice} - {descricao} - {data}')
                print("=" * 30)
        remover = int(input("EXCLUIR QUAL TAREFA? Nº: "))
        print("=" * 30)
        if remover <= 0 or remover > len(tarefas):
            print("TAREFA INEXISTENTE!!!")
        else:
            removida = tarefas.pop(remover - 1)
            print(f"TAREFA {removida['tarefa']} REMOVIDA COM SUCESSO!!!")
    return

def verificar_tarefas_pendentes(tarefas):
    fuso_horario = timezone("America/Sao_Paulo")
    data_hoje = datetime.now(fuso_horario).strftime('%d/%m/%Y')
    tarefa_hoje = [tarefa for tarefa in tarefas if tarefa['data'] == data_hoje]
    if tarefa_hoje:
        for tarefa in tarefa_hoje:
            print(f"TAREFA DE HOJE: {tarefa['tarefa']}")
    else:
        print("NÃO TEM TAREFAS PRA HOJE!!!")  
    return

if __name__ == "__main__":
    main()

