v1=[]
contagem=0
for i in range(3):
    v1.append(input("digite algo: "))
for j in range (len(v1)):
    if (v1.count(v1[j]))>1:
        contagem+=1
v=len(v1)
resultado= v - contagem
print(resultado)