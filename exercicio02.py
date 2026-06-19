#Exercício 2: Radar de Velocidade Eletrônico
#Enunciado: Desenvolva um script que leia a velocidade de um carro em km/h.
# Se o carro ultrapassar 80 km/h, exiba uma mensagem dizendo que ele foi multado.
# Se ele estiver dentro do limite, exiba uma mensagem de "Boa viagem, dirija com segurança!".

veloci = int(input("Leitura da velocidade : "))

if veloci > 80  :
    print(f"MULTADO!Velocidade de {veloci} km")
else :
    print(f"Boa viagem, dirija com segurança!Velocidade de {veloci} km")



