'''
Fabio Pilon 0391/22-1
sequencia de fibonacci recursiva e com laço for

'''


# def fibonacci(n):   
#     if n <= 1:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)
        
# def main():
#     #x = int(input("valor de n: "))
#     for i in range (20):
#         print(fibonacci(i))

# main()



def fib(n):
    a = 0
    b = 1
    if n == 1:
        print (a)
    else:
        print(a)
        print(b)
    
    for i in range(2,n):
        c = a+b
        a=b
        b=c

        print (c)
fib(20)

