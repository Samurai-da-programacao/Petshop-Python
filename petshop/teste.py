
usuarios = {}

def menu_principal():
    while True:
        print("\n--- Menu Principal ---")
        print("1. Cadastro")
        print("2. Login")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastro()
        elif opcao == "2":
            if login():
                break  # Encerrar o programa após o login e a exibição do resumo
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

def cadastro():
    print("\n--- Cadastro ---")
    nome = input("Digite seu nome: ")
    nome_animal = input("Digite o nome do seu animal: ")
    cpf = input("Digite seu CPF: ")
    email = input("Digite seu e-mail: ")
    senha = input("Crie uma senha: ")
    
    
    usuarios[email] = {
        "nome": nome,
        "nome_animal": nome_animal,
        "cpf": cpf,
        "senha": senha
    }
    print("Cadastro realizado com sucesso!")

def login():
    print("\n--- Login ---")
    email = input("Digite seu e-mail: ")
    senha = input("Digite sua senha: ")
    
    # Verificar se o e-mail existe e se a senha está correta
    if email in usuarios and usuarios[email]["senha"] == senha:
        print("Login realizado com sucesso!")
        escolher_servico(email)
        return True
    else:
        print("Usuário não encontrado.")
        return False

def escolher_servico(email):
    print("\n--- Escolha de Serviço ---")
    print("1. Banho (30 reais)")
    print("2. Tosa (40 reais)")
    print("3. Banho e Tosa (80 reais)")
    servico_opcao = input("Escolha uma opção: ")
    
    # serviços
    servicos = {
        "1": ("Banho", 30),
        "2": ("Tosa", 40),
        "3": ("Banho e Tosa", 80)
    }
    
    if servico_opcao in servicos:
        servico, preco = servicos[servico_opcao]
        usuarios[email]["servico"] = servico
        usuarios[email]["preco"] = preco
        escolher_horario(email)
    else:
        print("Opção de serviço inválida, tente novamente.")
        escolher_servico(email)

def escolher_horario(email):
    print("\n--- Escolha de Horário ---")
    print("1. 13:00")
    print("2. 15:00")
    print("3. 17:00")
    horario_opcao = input("Escolha um horário: ")
    
    # Escolhas de horario
    horarios = {
        "1": "13:00",
        "2": "15:00",
        "3": "17:00"
    }
    
    if horario_opcao in horarios:
        usuarios[email]["horario"] = horarios[horario_opcao]
        resumo(email)
    else:
        print("Opção de horário inválida, tente novamente.")
        escolher_horario(email)

def resumo(email):
    print("\n--- Resumo ---")
    print(f"Nome: {usuarios[email]['nome']}")
    print(f"Nome do Animal: {usuarios[email]['nome_animal']}")
    print(f"Serviço escolhido: {usuarios[email]['servico']} - R$ {usuarios[email]['preco']}")
    print(f"Horário escolhido: {usuarios[email]['horario']}")
    print("Obrigado pela sua confiança!!!")
    print("\n--- Encerrando o programa ---")


menu_principal()