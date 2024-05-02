#Desafio 028 - Programa que pense em um número de 0 a 5 e faça com que o usuário tente adivinhar

from random import randint
ae = randint(0, 5)
n1 = int(input("Tente descobrir qual foi o número (entre 0 e 5) escolhido pelo computador: ").strip())
if n1 > 5:
    print("Número inválido")
else:
    print("Parabéns, você adivinhou certo!") if n1 == ae else print("Que pena, não foi dessa vez!")

#Desafio 029 - Programa que calcula multas a velocidades acima de 80km/h

v = int(input("Em qual velocidade você estava? ").strip())
if v > 80:
    m = (v - 80) + 6
    print("Você vai pagar {}R$ de multa!".format(m))

#Desafio 030 - Programa que diz se um número é par ou ímpar

n2 = int(input("Digite qualquer número inteiro: ").strip())
print("Este número é par") if n2 % 2 == 0 else print("Este número é ímpar")

#Desafio 031 - Programa que calcula o preço de uma viagem (0,50¢ por Km) e 0,45¢ se esta viagem ter mais de 200Km

vk = int(input("Digite qual a distância da sua viagem em Km: ").strip())
if vk >= 200:
    vk = vk * 0.45
    print("Você vai pagar {}R$ nessa viagem".format(vk))
else:
    vk = vk * 0.50
    print("Você vai pagar {}R$ nessa viagem".format(vk))

#Desafio 032 - Programa que calcula anos bissextos

ano = int(input("Digite algum ano: ").strip())
print("Este ano é bissexto") if ano % 4 == 0 and ano % 100 != 0 else print("Este ano não é bissexto")

#Desafio 033 - Programa que mostra o maior número

nu1 = int(input("Digite apenas um algarismo: ").strip())
nu2 = int(input("Digite apenas um algarismo: ").strip())
nu3 = int(input("Digite apenas um algarismo: ").strip())
if nu1 > nu2 > nu3:
    print("{} Este é o maior valor".format(nu1))
elif nu2 > nu1 > nu3:
    print("{} Este é o maior valor".format(nu2))
else:
    print("{} Este é o maior valor".format(nu3))

#Desafio 034 - Programa que aumenta o aumento do salário

sal = float(input("Digite o seu salário: ").strip())
if sal > 1250:
    aum = (10 * sal) / 100
    print("Você recebeu um aumento de {}R$".format(aum))
elif sal <= 1250:
    aum = (15 * sal) / 100
    print("Você recebeu um aumento de {}R$".format(aum))

#Desafio 035 - Calcular comprimentos de retas e ver se elas podem formar um triângulo

r1 = float(input("Diga qual o comprimento de uma reta: ").strip())
r2 = float(input("Diga qual o comprimento de uma reta: ").strip())
r3 = float(input("Diga qual o comprimento de uma reta: ").strip())
if (r2 - r3) < r1 < r2 + r3 and (r1 - r3) < r2 < r1 + r3 and (r1 - r2) < r3 < r1 + r2:
    print("Estas retas podem formar um triângulo!")
else:
    print("Estas retas não podem formar um triângulo!")
