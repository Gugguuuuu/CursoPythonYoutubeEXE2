n = float(input('Digite um numero : '))
n1 = n
continuar = str(input('Você quer continuar ( S | N ) : ')).strip().upper()
maior = n
menor = n
i = 0
media = 0
soma_n = 0
while continuar == 'S':
    n = float(input('Digite outro numero : '))
    if n > maior:
        maior = n
    elif n < menor:
        menor = n
    i += 1
    soma_n += n
    continuar = str(input('Você ainda quer continuar ( S | N) : ')).strip().upper()
media = (soma_n + n1) /(i + 1)
print('\033[34mCom base nesses numeros temos os dados : \nO maior numero digitado foi : \033[35m{:.2f}\033[m\n\033[34mO menor foi    :\033[m \033[35m{:.2f}\033[m\n\033[34mE a media total foi :\033[m \033[35m{:.2f}\033[m'.format(maior, menor, media))