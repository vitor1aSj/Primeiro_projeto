# Exercício 8
valor_compra = float(input("Digite o valor total das compras: R$ "))
desconto = 0
if valor_compra <= 100:
    desconto = 0
elif valor_compra <= 300:
    desconto = valor_compra * 0.05
elif valor_compra <= 500:
    desconto = valor_compra * 0.10
else:
    desconto = valor_compra * 0.15

total_final = valor_compra - desconto

print("Resumo da compra ")
print(f"Valor original: R$ {valor_compra:.2f}")
print(f"Desconto: R$ {desconto:.2f}")
print(f"Total a pagar: R$ {total_final:.2f}")
