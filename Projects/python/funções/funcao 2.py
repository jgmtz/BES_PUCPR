def nunber(n):
    for num in range(1,n+1):
        for i in range(1, num+ 1):
            print(i, end=' ')
        print()


n = int(input('Quantos valores voce gostaria: '))
nunber(n)