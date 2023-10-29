def numbers(n):
    try:
        n = int(n)
        if n < 0:
            print('Please enter a positive number')
        else:
            cnt = 0
            for i in range(1,n +1):
                if i % 3 == 0:
                    cnt += 1
        print('numbers divisible by 3 among numbers from 1 to ', n, ': ', cnt)                   
    except:
        print('Please enter a positive number')
while True:
    x = input('Enter a positive integer : ')
    if x == 'done':
        print('Bye Bye')
        break
    else:
        numbers(x)