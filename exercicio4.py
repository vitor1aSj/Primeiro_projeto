#Exercício 4: Validador de Acesso a Conteúdo
#Enunciado: Um site de streaming possui conteúdos restritos por idade.
# Escreva um programa que peça o ano de nascimento do usuário.
# O script deve calcular a idade dele (considerando o ano atual como 2026).
# Se o usuário tiver 16 anos ou mais, o acesso ao filme está liberado.
# Caso contrário, exiba a mensagem: "Acesso bloqueado: Conteúdo não recomendado para menores de 16 anos."

ano_nasc = int(input("Digite a sua data de nascimento: "))

calculo = ano_nasc - 2026

if ano_nasc >= 16 :
    print(f"Acesso liberado!Você tem {calculo}!")
else :
    print(f"Acesso bloqueado: Conteudo não recomendado para menores de 16 anos {calculo}!")