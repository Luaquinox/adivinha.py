print ("*************************")
print ("Bem vindo ao adivinhe.py")
print ("*************************")

chute=int(input("Digite seu número:"))
numero_secreto = 17
acertou = chute == numero_secreto
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

 
print(f"Você digitou {chute}")
  
if(acertou):
  print("Você Acertou!")
else:
 if(chute_maior):
  print("Você Errou! Seu número foi maior que o número secreto")
if(chute_menor):
 print("Você Errou! Seu número foi menor que o número secreto")

print("***********")
print("Fim de Jogo")
print("***********")
