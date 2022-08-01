def fibonacci(numero):
    if (numero==1) or (numero==2):
        print("Pertence a sequencia")
    else:
        ult = 1
        penult = 1
        atual = 1
        while atual < numero:
            atual = ult + penult
            penult = ult
            ult = atual
        if atual == numero:
            print("Pertence a sequencia")
        else: 
            print("Nao pertence a sequencia")

if __name__ == "__main__":
    numero = int(input("Numero que deseja verificar se esta na sequencia: "))
    fibonacci(numero)