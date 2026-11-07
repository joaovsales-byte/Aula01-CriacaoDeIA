valor_compra = int(input("Insira o valor da compra: "))
cupom = input("Insira o cupom: ")

if valor_compra > 300 or cupom == "PROMO10":
    print("Promoção aplicada com sucesso!")
else:
    ("Nenhuma promoção desponível")