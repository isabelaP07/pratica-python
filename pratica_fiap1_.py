print("Saudações\033[1;35;40mJedi\033[0m\nViemos numa missão de\t\033[1;32;40mpaz\033[0m")

nome = input("Informe seu nome: ")
lugar = input("Informe o lugar: ")
print(f'Bem-vindo {nome:>20}!\nVocê chegou em {lugar:#^30}.')

saudacao = 'Bem-vindo {}!'.format('Jedi')
print(saudacao)