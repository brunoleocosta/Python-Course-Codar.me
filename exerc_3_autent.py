USUARIO = "admin"
SENHA = "123123"

# Solicita o nome de usuário e senha
nome_usuario = input("Digite o nome do usuário: \n")
senha = input("Digite a senha: \n")

# Verifica se o nome de usuário e a senha estão corretos
if nome_usuario == USUARIO and senha == SENHA:
    print("Autenticação foi bem-sucedida.")
elif nome_usuario != USUARIO:
    print("Usuário não existe.")
else:
    print("Senha incorreta.")