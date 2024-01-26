# EXERCICIO 62
p = int(input('Digite o primeiro termo : '))
r = int(input('Digite a razão : '))
t = int(input('Digite quantos termos você quer : '))
t = p + (t - 1) * r
while r <= t:
    print('\033[34m{}\033[m'.format(r), end=' \033[33m->\033[m ')
    r += 2
print('FIM')