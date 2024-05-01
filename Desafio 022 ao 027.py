#Desafio 022 - Ler o nome completo de uma pessoa e mostrar: O nome com todas as letras maiúsculas; O O nome com todas as letras minúsculas; Quantas letras tem ao todo (Desconsiderando espaços); Quantas letras tem o primeiro nome.

nome = input("Digite seu nome completo: ").strip()
print("O nome com todas as letras maiúsculas, fica:", nome.upper())
print("O nome com todas as letras minúsculas, fica:", nome.lower())
print("Seu nome tem {} letras".format(len(nome.replace(" ", ""))))
print("Seu primeiro nome tem {} letras".format(len(nome.split()[0])))

#Desafio 023 - Ler um número de 0 a 9999 e mostrar cada um dos dígitos separados.

numero = input("Digite um número que vai de 0 a 9999: ").strip()
print("A Unidade de Milhar é",numero[0])
print("A Unidade de Centena é", numero[1])
print("A Unidade de Dezena é", numero[2])
print("A Unidade é:", numero[3])

#Desafio 024 - Ler o nome de uma cidade, e ver se ela começa com a palavra "Santo"

cidade = input("Diga o nome de alguma cidade: ").strip().upper()
print(cidade[:5] == ("SANTO"))

#Desafio 025 - Ler o nome de alguém, e saber se essa pessoa tem "Silva" no nome

nome2 = input("Digite seu nome: ").strip().upper()
print("SILVA" in nome2)

#Desafio 026 - Ler uma frase e mostrar: Quantas vezes aparece o "A", e em que posição ele aparece pela primeira e última vez

frase = input("Digite uma frase: ").strip().lower()
print("A sua frase tem {} letras 'a'".format(frase.count('a')))
print("A primeira vez que a letra 'a' aparece é na posição:", frase.find('a')+1)
print("A última vez que a letra 'a' aparece é na posição:", frase.rfind('a')+1)

#Desafio 027 - Ler um nome, e mostrar o primeiro e o último nome, separadamente

nome3 = input("Digite seu nome: ").strip().split()
print("O seu primeiro nome é {}\nE o último é {}".format(nome3[0], nome3[-1]))
