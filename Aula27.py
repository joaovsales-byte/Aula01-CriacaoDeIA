senha_correta = "python123"
tentativa = 0

while tentativa < 3:
    senha = input("Digite sua senha: ")
    if senha == senha_correta:
        print("Acesso liberado!")
        break
    else:
        print("Senha icorreta")
    tentativa += 1
else:
    print('Limite de tentativas atingido')