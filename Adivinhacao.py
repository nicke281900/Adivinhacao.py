print("***********************")
print("adivinhacao")
print("***********************")



numero_secreto = 24
acertou = numero_secreto == chute
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

chute = int(input("Digite o seu Número: "))

print(f"Você digitou {chute}")

if(acertou):
    print("Você acertou!")
else:
    if(chute_maior):
        print("você errou! Seu número foi maior que o numero secreto")
    elif(chute_menor):
        print("você errou! Seu número foi menor que o numero secreto")

    print("@@@@@@@@@@@")
    print("fim de Jogo")
    print("@@@@@@@@@@@")