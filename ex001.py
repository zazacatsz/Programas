#Faça um programa que leia dois vetores de 3 posições que representam forças sobre um ponto no espaço 3D, e escreva a força resultante. 
v1=[]
v2=[]
for i in range (3):
    v1.append(float(input(f"digite um número para o vetor1 posição{i}:  ")))
    v2.append(float(input(f"digite um número para o vetor2 posição{i}:  ")))
for j in range (3):
    print(f"A força resultante {j} é:{v1[j]+v2[j]}")