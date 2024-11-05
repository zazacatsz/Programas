'''Primeiro Trabalho ACED
Integrantes do Grupo:
Miguel Farias Moreira Do Casal
Yuri Abilio de Moura
Charlie Bartholo Christo Rocha
João Marcos Peixoto do Nascimento
Roger Vinícius Pereira Augusto
'''
#Questão 2:
#Faça um programa que leia um número inteiro positivo e mostre a figura abaixo na tela
valor = int(input("Escolha um número:"))
line= 1

while (line<=valor):
        n1 = 0
        n2 = 0
        nAtual = 1
        count = 1

        while(count <= line):
            res=1
            aux=1


            while (aux<=nAtual):
                res *= aux
                aux+= 1
            print(f'{nAtual}!={res}', end="  ")

            n1 = n2
            n2 = nAtual
            nAtual = n1 + n2
            count+=1
        print()
        line+=1




