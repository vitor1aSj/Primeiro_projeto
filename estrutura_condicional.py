#comer ou passar fome?

print(" Comer ou passar fome ?")

resposta = input("Você ta com fome?: s/n")
if resposta == "s" :
    print("Então se aliemente!")
    tem_dinheiro = input("Você tem dinheiro?: s/n")
    if tem_dinheiro == "s" :
        print("Compre o lanche!")
    else: print("Não compre!")
else: print("Não se alimente!")







