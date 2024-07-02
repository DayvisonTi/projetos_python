"""
Faça uma lista de compras com listas
oo usuario deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erro de indices inexistentes na lista

"""
lista_compras = []

while True:
    opcao = input("""Selecione uma opção\n[i]nserir [a]pagar [l]istar: """).lower()[0]
    inserir = True if opcao == "i" else False
    apagar = True if opcao == "a" else False
    listar = True if opcao == "l" else False
    if inserir:
        valor = input("Valor: ").title()
        lista_compras.append(valor)
        continue
    elif apagar:
        for i, item in enumerate(lista_compras):
            print(i, item)
        indice = int(input("Escolha o indice para apagar: "))
        try:
            print(f"{lista_compras[indice]} removida com sucesso.")
            lista_compras.pop(indice)
        except (IndexError, ValueError):
            print("Não foi possivel apagar este indice!!!")
            continue
    elif listar:
        if len(lista_compras) >= 1:
            for i, item in enumerate(lista_compras):
                print(i, item)
        else:
            print("Voçê ainda não adicionou itens a lista!!!")
    else:
        print("OPÇÃO INVALIDA...TENTE NOVAMENTE!!!")
    

