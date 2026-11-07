idade = int(input("Digite a idade: "))
tem_cnh = input("Tem CNH: ")

if idade >= 18 and tem_cnh == "sim":
    print("Pode dirigir")
else:
    print("Não pode dirigir")