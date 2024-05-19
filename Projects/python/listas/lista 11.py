'''Altere o programa anterior, intercalando 3 vetores de 10 elementos cada'''
vet1 = []
vet2 = []
vet3 = []
vet4 = []
for i in range(10):
    nums1 = int(input('insira um numero: '))
    nums2 = int(input('insira um numero: '))
    nums3 = int(input('insira um numero: '))
    vet1.append(nums1)
    vet2.append(nums2)
    vet3.append(nums3)
    vet4.append(vet1[i])
    vet4.append(vet2[i])
    vet4.append(vet3[i])
print(vet4)