nota1 = float(input("Digite a primeira nota:"))  #8.5
nota2 = float(input("Digite a segunda nota :"))
nota3 = float(input("Digite a terceira nota:"))

media = (nota1 + nota2 + nota3) / 3

if media >= 7 :
    print(f"Aluno(a) Aprovado!Com a media: {media:.2f}")
elif media >= 3 and media < 7:
    print(f"Aluno em recuperação com media {media:.2f}")
else: print(f"Aluno(a) Reprovado!Com a media:{media:.2f}")

