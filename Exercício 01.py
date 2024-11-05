#Faça um programa que leia um número inteiro qualquer e em seguida diga se cada um dos dígitos é par ou ímpar.
#Integrantes do Grupo:
#Miguel Farias Moreira Do Casal
#yuri Abilio de Moura
#Charlie Bartholo Christo Rocha
#João Marcos Peixoto do Nascimento
#Roger Vinícius Pereira Augusto
#Turma: 2BINFO
num=int(input('Digite um número qualquer: '))
n=str(num)
i=len(n)-1
while (i>-1):
    alg=num//10**i-(num//(10**(i+1)))*10
    if alg%2==0:
        print(f'{alg} é um número par')
        i-=1
    else:
        print(f'{alg} é um número ímpar')
        i-=1