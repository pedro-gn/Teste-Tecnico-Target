number = int(input("Insira um numero: "))

fib_number1 = 0
fib_number2 = 1

#Lida com o caso do numero ser 0 ou 1 que são os iniciais
if number in [fib_number1 , fib_number2]:
    print("Numero esta na sequencia")
    exit()

#Lida com qualquer outro caso
while number > fib_number2 :
    new_fib_n = fib_number1 + fib_number2
    fib_number1 = fib_number2
    fib_number2 = new_fib_n
    if number == new_fib_n :
        print("Numero esta na sequencia")
        break
else:
    print("Numero não está na sequencia")