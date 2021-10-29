j = 7
for i in range(1, 10):
    if i%2==1:
        print('I={} J={}'.format(i,j))
        print('I={} J={}'.format(i,j-1))
        print('I={} J={}'.format(i,j-2))
        j = j+2