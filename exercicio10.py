#Exercício 10: O Cálculo do IMC com Diagnóstico Completo
#Enunciado: Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
# O script deve pedir o peso (em kg) e a altura (em metros).
# O cálculo é feito pela fórmula: IMC = peso / (altura * altura) .
# Após calcular o valor do IMC, utilize uma estrutura encadeada de if/elif/else para exibir o diagnóstico exato:
# Abaixo de 18.5: Abaixo do peso•
# Entre 18.5 e
# 24.9: Peso ideal (parabéns)
#  Entre 25.0 e 29.9: Levemente acima do peso
# Entre 30.0 e 34.9: Obesidade Grau I
# Acima de 35.0: Obesidade Severa/Mórbida

peso = float(input("Digite seu peso em kg:"))
altura = float(input("Digite sua altura em metros:"))

imc = peso / (altura * altura)

print(f"Seu valor em imc é:{imc:.2f}")

if imc < 18.5 :
    print(f"Abaixo do peso! {imc:.2f}")
elif imc <= 24.9 :
    print(f"Peso ideal parabéns! {imc:.2f}")
elif imc <= 29.9:
    print(f"Levemente acima do peso! {imc:.2f}")
elif imc <=34.9:
    print(f"Obesidade grau I {imc:.2f}")
else:
    print(f"Obesidade Severa/Mórbida {imc:.2f}")



