 #O split gera uma lista com todas as palavras na cadeia de caracteres
# len- é o tamanho da palavra
# nome=(input('Digite seu nome: ')).strip()

# print('Carregando seu nome...')
# print('Esse é o seu nome com todas as letras maiúsculas : {}'.format(nome.upper()))
# print('Esse é o seu nome com todas as letras minúsculas : {}'.format(nome.lower()))
# separa=nome.split()
# print(separa)
# print('Esse é o seu nome com todas as letras separadas {}'.format('-'.join(nome)))
# print('Seu nome tem ao todo {} letras'.format(len(nome)-nome.count(' ')))
# print('Seu primeiro nome têm ao todo {} letras'.format(nome.find(' ')))


nome=str(input('Digite seu nome completo:')).strip()
nome=nome.split()
print('Seu primeiro nome é: {} '.format(nome[0]))
print('Seu último nome é:  {}'.format(nome[len(nome)-1]))