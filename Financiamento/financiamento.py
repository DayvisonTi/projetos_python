def casa():
    valor_casa = float(input('Valor da Casa: R$'))
    salario = float(input('Salário: R$'))
    quant_anos = int(input('Quantos anos de Financiamento? '))
    calculo(valor_casa,salario,quant_anos)


def calculo(valor_casa,salario,quant_anos):
    base = salario * 30 / 100
    prest = valor_casa / (quant_anos * 12)
    
    if prest >= base:
        print(f'A prestação tem que ser no minimo 30% do salario.')
        print(f'No seu salario a porcentagem fica em R${base:.2f}.')
        print(f'E a prestação fica em R${prest:.2f}.')
        print('Financiamento NEGADO!!!')
    else:
        print(f'A prestação tem que ser no minimo 30% do salario.')
        print(f'No seu salario a porcentagem fica em R${base:.2f}.')
        print(f'E a prestação fica em R${prest:.2f}.')
        print('Financiamento APROVADO!!!')
    return pergunta()


def pergunta():

   while True: 
        perg = input('Quer tentar novamente? [S/N] ').upper().strip()
        if perg == 'S':
            return casa()
        elif perg == 'N':
            print('Volte Sempre!!!')
            break
        else:
            print('Opção Invalida,tente novamente...')

casa()