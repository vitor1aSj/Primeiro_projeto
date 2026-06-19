#Exercício 6: Classificação de Atletas por Categoria
#Enunciado: A confederação de natação precisa de um sistema para classificar seus nadadores de acordo com a idade.
# Desenvolva um programa que leia a idade de um atleta e mostre sua categoria:
# Até 9 anos: Mirim
# Até 14 anos: Infantil
# Até 19 anos: Junior
# Até 25 anos: Sênior
# Acima de 25 anos: Master

idade = int(input("Digite sua idade : "))

if idade == 9 :
    print("Mirim")
elif idade == 14 :
    print("Infantil")
elif idade == 19 :
    print("Junior")
elif idade == 25 :
    print("Sênior")
else :
    print("Master")
