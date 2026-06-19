#Exercício 7: Analisador de Triângulos
#Enunciado: Para exercitar a lógica matemática, peça para o usuário digitar o comprimento de três retas (A, B e C).
# Primeiro, o programa deve verificar se essas retas podem formar um triângulo
# (Regra: a soma de dois lados deve ser sempre maior que o terceiro).
# Se formarem, o programa deve usar o elif para dizer que tipo de triângulo ele é:
# • Equilátero: todos os lados iguais.
# • Isósceles: dois lados iguais.
# • Escaleno: todos os lados diferentes.


print("DIGITE O COMPRIMENTO DE TRES RETAS: ")
retaA = int(input("Reta A :"))
retaB = int(input("Reta B :"))
retaC = int(input("Reta C :"))

soma= retaA + retaB > retaC

if retaA == retaB == retaC :
    print("Equilátero!")
elif retaA == retaB or retaA == retaC or retaB == retaC :
    print("Isósceles!")
else:
    print("Todos os lados são diferentes")


