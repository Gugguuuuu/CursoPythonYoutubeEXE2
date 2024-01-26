# EXERCICIO 64
print('\033[1;2;7;37;40mDigite alguns numeros e você vera a soma de todos e digite [ 999 ] para encerra o progama\033[m')
n = int(input('Digite um numero : '))
soma = 0
while n != 999:
    if n != 999:
        soma += n
    n = int(input('Digite outro numero : '))
print('\033[1;34mA soma de todos esses numeros é\033[m \033[1;35m{}\033[m'.format(soma))