'''
Yuri Abilio De Moura
João Marcos Peixoto do Nascimento
Miguel Farias Moreira do Casal
Roger Vinícius Pereira Augusto
'''
c5=0
j=int(input('Digite um número binario de 4 digitos:\n'))
k=int(input('Digite um número binario de 4 digitos:\n'))
ab=j+k
n4=ab//1000
n3=(ab-(n4*1000))//100
n2=(ab-(n4*1000+n3*100))//10
n1=(ab-(n4*1000+n3*100+n2*10))

if (n1==2):

    n2+=1
    n1=0

if(n2==2):

    n3+=1
    n2=0

elif(n2 == 3):

    n3+=1
    n2=1

if(n3 == 2):

    n4+=1
    n3=0

elif(n3 == 3):

    n4+=1
    n3=1

if(n4==2):

    n5=1
    n4=0

elif(n4==3):

    n5=1
    n4=1

if(c5!=0):
    print(f'A soma é igual a: {n5}{n4}{n3}{n2}{n1}')

else:
    print(f'A soma é igual a: {n4}{n3}{n2}{n1}')