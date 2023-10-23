#Exercício Python 09: faça um software que verifique entre 2 numeros qual o maior
n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
if n1 > n2:
    print(f"O numero {n1} é maior que o numero {n2}")
elif n2 > n1:
    print(f"O numero {n2} é maior que o numero {n1}")