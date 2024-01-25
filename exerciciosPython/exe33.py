# EXERCICIO 33
ask = str(input('Você vai fazer compras? '.strip().lower()))
if ask == 's' or ask == 'sim':
   i = 1
   compras = float(input('Digite o valor da sua {}° compra : '.format(i)))
   continuar = str(input('Você fez mais compras? '))
   if continuar == 'sim' or continuar == 's':
      continuar == True
while continuar == True:
   i = 1 + 1
   compras = float(input('Digite o valor de {}° compra'.format(i)))
   media = compras
print(compras)
