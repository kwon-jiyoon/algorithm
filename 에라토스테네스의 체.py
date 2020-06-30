def prime(n):
    check = [False] * n

    for i in range(2,n):
        if check[i] == False:
            for j in range(i+i, n, i):
                check[j] = True

    return [i for i in range(2,n) if check[i] == False]
