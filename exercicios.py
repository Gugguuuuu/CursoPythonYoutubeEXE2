# import pyautogui
# import time
# i = 2
# for i in range(25):
#     i = i + 1
#     pyautogui.click(x=155, y=92)
#     pyautogui.write('exe{}.py'.format(i))
#     pyautogui.press('enter')
# lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# for i, n in enumerate(lista):
#     print(i+1, n)
nome = str(input('Digite seu nome : ')).strip().title()
sexo = str(input('Digite seu sexo ( M | F ) : ')).strip().upper()
while sexo != 'M' and sexo != 'F':
    print('\033[31mDIGITE UM SEXO VALIDO VOCÊ NÃO É UMA GELADEIRA DE 4 PORTAS\033[m')
    sexo = str(input('Digite seu sexo ( M | F) : '))
if sexo == 'F':
    sexo = '\033[35mFeminino\033[m'
else:
    sexo = '\033[34mMasculino\033[m'
print('Olá {}, seu sexo é {}'.format(nome, sexo))