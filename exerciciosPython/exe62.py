# EXERCICIO 62
p = int(input('Digite qual vai ser o primeiro termo : '))
r = int(input('Digite qual vai ser a razão : '))
t = int(input('Digite quantos termos você quer : '))
t = t * 2
tot = 0
while r <= t:
    print('\033[34m{}\033[m'.format(r), end=' \033[33m->\033[m ')
    r += 2
    tot = r
m = int(input('Você quer mais quantos termos : '))
t = t + m
while tot <= t:
    print('\033[34m{}\033[m'.format(tot), end=' \033[33m->\033[m ')
    tot += 2   
