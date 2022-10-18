# Nome: Fabio Pilon 0391/22-1
       
# um numero primp é divisivel por 1 e por ele mesmo
# crie um algoritmo que solicite um valor limite com até 4 digitos (0-9999)
# busque todos os primos ate o valor limite
#guardar numa matriz de 1 dimensao
# ao final mostrar o total de numeros primos somados e a somatoria deles

soma = 0
numero = 0
matriz_de_primos = []


while numero < 2:
    
    numero = int(input("digite o valor limite: "))
    if (numero > 9999):
        break

for x in range(0,numero+1):
    #inicia o numero de divisores que o proximo numero tem
    div = 0
    for y in range(1,x+1):
        #verifica a quantidade de divisores
        if (x % y == 0):
            div +=1
    #se a quantidade for 2, no caso, 1 e o proprio numero, coloca em um array
    if div == 2:
        matriz_de_primos.append(x)
        soma += x
print(matriz_de_primos)
print("a soma dos numeros é: ", soma)




