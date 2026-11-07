idade = int(input("Digite a idade: "))
estudante = input("Você é estidante?")

if idade < 12 or estudante == "s":
    print("Entrada gratuita")
else:
    print("Entrada paga")