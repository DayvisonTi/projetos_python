import os

usuarios = []
contas = []
AGENCIA = '0001'
num_conta = len(contas) + 1

usuario = dict(
    {'nome': 'Dayvison',
    'cpf': '09623032404',
    'email': 'dayvisonlacerda@hotmail.com'}
    )
usuario2 = dict({'nome': 'Cassia',
    'cpf': '01593446462',
    'email': 'cassia.dmi@hotmail.com'})

usuarios.append(usuario)
usuarios.append(usuario2)

os.system('clear')

for conta in range(1,6):

    cpf = '09623032404'

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario['conta'] = []
            contas.append(num_conta)
            usuario['conta'].append(num_conta)
            usuario['agencia'] = AGENCIA

    cpf = '01593446462'

    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            usuario['conta'] = []
            contas.append(num_conta)
            usuario['conta'].append(num_conta)
            usuario['agencia'] = AGENCIA
            
            print(usuario)
for user in usuarios:
    for chave,valor in user.items():
        print(f'{chave} - {valor}')

    
    
