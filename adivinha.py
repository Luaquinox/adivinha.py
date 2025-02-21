print("**************************")
print("Bem vindo Jogo da Adivinha")
print("**************************")


chute = int(input("Digitem o seu número: "))
numero_secreto = 19
acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

print(f"Você digitou {chute}")

if(acertou):
   print("Você acertou!")
else:
 if (chute_maior):
  print("Você errou! seu número foi maior que número secreto")
 if ( chute_menor):
    print("Você errou! seu número foi menor que número secreto")


print("@@@@@@@@@@@")
print("Fim de jogo")
print("@@@@@@@@@@@")
