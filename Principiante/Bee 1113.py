while True:
    try:
        a, b = list(map(int, input().split()))
        if a == b:
            break
        else:
            if a > b:
                print('Decrescente')
            else:
                print('Crescente')
    except EOFError:
        break
