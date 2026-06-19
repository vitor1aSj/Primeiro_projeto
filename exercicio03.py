#Exercício 3: Classificador de Temperatura
#Enunciado: Crie um programa que receba a temperatura atual de uma cidade (em graus Celsius) e classifique
# o clima baseado nas regras abaixo usando if, elif e else:
# Menor que 15°C: "Clima Frio"•
# Entre 15°C e 25°C: "Clima Agradável"•
# Maior que 25°C: "Clima Quente"

temp = int(input("Digite a temperatura atual da cidade :"))

if temp < 15 :
    print(f"Clima frio: {temp}°")
elif temp >= 15 and 25 > temp:
    print(f"Clima Agradavél:{temp}°")
else:
    print(f"Clima quente!:{temp}°")


