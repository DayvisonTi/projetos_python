import yaml


while True:
    nome = input('Nome: ')
    trabalho = input('Trabalho: ')
    nacionalidade = input('Nacionalidade: ')
    idade = input('Idade: ')
    linguagens = input('Linguagens: ')
    experiencias = input('Experiencias: ')

  
    data = {
    'usuarios':{
    'Nome': nome,
    'Area Profissional': trabalho,
    'Nacionalidade': nacionalidade,
    'Idade': idade,
    }
    
}   
    data['Linguagens'] = linguagens
    data['Experiencias'] = experiencias

    arquivo = 'dados.yaml'
        
    with open(arquivo, 'a+', encoding='utf-8') as arquivo:
        yaml_output = yaml.dump(data, arquivo, sort_keys=False, allow_unicode=True, de) 


    arquivo.close()

    break
 



