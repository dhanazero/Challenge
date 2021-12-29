def dungPret(a):
    c = a+1
    for b in range(1, c):
        if b % 3 == 0 and b % 5 == 0:
            print('DungPrett')
        elif b % 3 == 0:
            print('Dung')
        elif b % 5 == 0:
            print('Prett')
        else:
            print(b)


dungPret(50)
