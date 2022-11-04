# fizzbuzz challenge
def fizzbuzz(n):
    for a in range(1, n+1):
        if a % 15 == 0:
            print('fizzbuzz')
        elif a % 3 == 0:
            print('fizz')
        elif a % 5 == 0:
            print('buzz')
        else:
            print(a)

if __name__=='__main__':
    fizzbuzz(30)

