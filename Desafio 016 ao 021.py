#Importação de bibliotecas - Porção inteira de um número

from math import trunc
n = float(input("Digite qualquer número real: "))
int = trunc(n)
print("O número {} com porção inteira é {}".format(n, int))

#Comprimento do Cateto Oposto, Adjacente, Triângulo Retângulo e Hipotenusa

from math import hypot
catop = float(input("Qual o comprimento do cateto oposto? "))
catad = float(input("Qual o comprimento do cateto adjacente? "))
hipot = hypot(catop, catad)
print("O comprimento da hipotenusa é {:.2f}".format(hipot))

# Seno, Cosseno e Tangente de um ângulo

from math import sin, cos, tan, radians
ang = float(input("Digite um ângulo: "))
seno = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print("O ângulo de {} tem o seno de: {:.2f}".format(ang, seno))
print("O ângulo de {} tem o cosseno de {:.2f}".format(ang, coss))
print("E tem a tangente de {:.2f}".format(ang, tang))

# Sortear um item de uma lista

from random import choice
pn = input("Digite um nome: ")
sn = input("Digite outro nome: ")
tn = input("Digite outro nome: ")
la = [pn, sn, tn,]
al = choice(la)
print("A pessoa sorteada foi:", al)

# Sortear um item de uma lista e organizá-la
 
import random
no1 = input("Digite um nome: ")
no2 = input("Digite outro nome: ")
no3 = input("Digite outro nome: ")
lista = [no1, no2, no3]
random.shuffle(lista)
print("A sequência de pessoas sorteadas é:", lista)

# Tocando música no Python

import playsound
playsound.playsound("/home/lucas/Downloads/Killing Yourself To Live - Black Sabbath.mp3")

