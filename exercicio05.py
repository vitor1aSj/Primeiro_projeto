#Exercício 5: Análise de Crédito Bancário Simplificada
#Crie um script que receba o salário bruto de um cliente e o valor da parcela do empréstimo que ele deseja pagar.
#O empréstimo só pode ser aprovado se o valor da parcela não ultrapassar 30% do salário bruto do cliente.
#Use if/else para exibir o resultado ("Crédito Aprovado" ou "Crédito Recusado").

salario_bruto= int(input("Digite o seu salário bruto:"))
valor_parcela = int(input("Digite o valor da parcela que deseja realizar o pagamento:"))

porcentagem_parcela = (salario_bruto * valor_parcela) / 100

if porcentagem_parcela <= 30:
    print(f"Aprovado!o valor da porcentagem foi {porcentagem_parcela}%")
else:
    print(f"Crédito recusado!Com: {porcentagem_parcela}%")

