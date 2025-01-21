print ('Qual é a sua idade?') 

idade_permitida = 18

idade_da_pessoa = input('Digite sua idade: ')

print('Sua idade é' , idade_da_pessoa)

idade_da_pessoa = int(idade_da_pessoa)

maior_de_idade = (idade_da_pessoa >= idade_permitida)

if (maior_de_idade):
    print("A idade é permitida.")
else:
    print("A idade não é permitida.")