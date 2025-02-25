print("**************************")
print("Bem vindo Jogo da Adivinha")
print("**************************")

numero_secreto = 19
total_de_tentativas = 3
rodada = 1

while (rodada <= total_de_tentativas):
   print(f"Tentativa {rodada} de {total_de_tentativas} ")
   chute = int(input("Digitem o seu número: "))

   acertou = chute == numero_secreto
   chute_maior = chute > numero_secreto
   chute_menor = chute < numero_secreto

   print(f"Você digitou {chute}")

   if(acertou):
      print("Você acertou!")
   else:
      if (chute_maior):
         print("Você errou! seu número foi maior que número secreto")
      if (chute_menor):
         print("Você errou! seu número foi menor que número secreto")

   rodada = rodada + 1

print("@@@@@@@@@@@")
print("Fim de jogo")
print("@@@@@@@@@@@")
