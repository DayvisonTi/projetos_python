import ruamel.yaml

def obter_dados_usuario():
    nome = input('Nome: ').title().strip()
    area_profissional = input('Area Profissional: ').title().strip()
    nacionalidade = input('Nacionalidade: ').title().strip()
    idade = input('Idade: ').title().strip()

    while True:
        linguagens = []
        ling_input = input('Linguagens: ')
        if ling_input.strip():
            linguagens = [ling.strip() for ling in ling_input.split(',')]
            nova_ling = input('Outra Linguagem? [S/N]: ').upper().strip()[0]
            if nova_ling == 'N':
                break
            else:
                continue
            
        elif not ling_input:
            break
        
    experiencias = []
    while True:
        experiencia = input('Experiências: ')
        if not experiencia:
            break
        experiencias.append(experiencia)
        while True:
            nova_exp = input('Quer adicionar mais alguma Experiencia? [S/N]').upper().strip()
            if nova_exp == 'N':
                break
            else:
                continue

            
        if nova_exp == 'N':
            break

    dados = {
    
    'nome': nome,
    'Profissão': area_profissional,
    'nacionalidade': nacionalidade,
    'idade': idade
    
    }    

    if linguagens:
        dados['Linguagens'] = linguagens

    if experiencias:
        dados['Experiencias'] = experiencias

    return dados

def salvar_arquivos(dados_usuario, nome_arquivo):

    with open(nome_arquivo, 'a+', encoding='utf-8') as arquivo:
        yaml = ruamel.yaml.YAML()
        yaml.dump([dados_usuario], arquivo)




dados_usuario = obter_dados_usuario()

nome_arquivo = 'dados.yaml'

salvar_arquivos(dados_usuario, nome_arquivo)