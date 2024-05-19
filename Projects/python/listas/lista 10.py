'''Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos
valores deverão ser compostos pelos elementos intercalados dos dois outros vetores'''
vet1 = []
vet2 = []
vet3 = []
for i in range(10):
    nums1 = int(input('insira um numero: '))
    nums2 = int(input('insira um numero: '))
    vet1.append(nums1)
    vet2.append(nums2)
    vet3.append(vet1[i])
    vet3.append(vet2[i])
print(vet3)