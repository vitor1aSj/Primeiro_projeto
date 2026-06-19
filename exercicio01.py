#Exercício 1:
# O Verificador de Paridade Enunciado: Escreva um programa que receba um número inteiro do usuário.
# Utilizando a estrutura if/else, verifique se o número é Par ou Ímpar e exiba uma mensagem correspondente no terminal.
#Dica: Use o operador de módulo % para verificar o resto da divisão por 2.


num = int(input("Digite um numero inteiro:"))

if num % 2 == 0 :
    print("Par!")
else:
    print("Impar!")

