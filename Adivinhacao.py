print("***********************")
print("adivinhacao")
print("***********************")

numero_secreto = 24
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas ):
    print(f"tentativa (rodada) de {total_de_tentativas}")
    chute = int(input("Digite o seu Número: "))

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto


    print(f"Você digitou {chute}")

    if(acertou):
        print("Você acertou!")
    else:
        if(chute_maior):
            print("você errou! Seu número foi maior que o numero secreto")
        elif(chute_menor):
            print("você errou! Seu número foi menor que o numero secreto")

        rodada = rodada + 1

    print("@@@@@@@@@@@")
    print("fim de Jogo")
    print("@@@@@@@@@@@")