from ast import Break
contas = []
def cadastro():
  nome = input("Digite o nome do usuário: ")
  email  = input("Digite o e-mail do usuário: ")
  telefone  = input("Digite o telefone do usuário: ")
  endereco  = input("Digite o endereco do usuário: ")
  escolha = []
  conta = {'nome': nome, 'email' : email, 'telefone' : telefone, 'endereco' : endereco, 'preferencias': nome}
  contas.append(conta)
  print("Sua conta foi criada com sucesso!")

def exibir_cadastro():
  numero_conta = int(input("Digite o número da conta que deseja acessar: "))
  if numero_conta >= 1 and numero_conta <= len(contas):
    conta = contas[numero_conta - 1]
  else:
      print("Conta não encontrada. Certifique-se de que o número da conta é válido.")
  print(f"\nNome: {conta['nome']}")
  print(f"E-mail: {conta['email']}")
  print(f"Telefone: {conta['telefone']}")
  print(f"Endereço: {conta['endereco']}")

def atualizar_cadastro():
  numero_conta = int(input("Digite o número da conta que deseja editar: "))
  if numero_conta >= 1 and numero_conta <= len(contas):
    conta = contas[numero_conta - 1]
    print("Conta encontrada.")
    novo_nome = input("Digite o novo nome (ou pressione Enter para manter o atual): ")
    if novo_nome:
      conta['nome'] = novo_nome
    novo_email = input("Digite o novo e-mail (ou pressione Enter para manter o atual): ")
    if novo_email:
      conta['email'] = (novo_email)
    novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
    if novo_telefone:
      conta['telefone'] = (novo_telefone)
    novo_endereco = input("Digite o novo endereço (ou pressione Enter para manter o atual): ")
    if novo_endereco:
      conta['endereco'] = (novo_endereco)
      print("Conta editada com sucesso!")
  else:
    print("Conta não encontrada. Certifique-se de que o número da conta é válido.")

def excluir_conta():
  numero_conta = int(input("Digite o número da conta que deseja excluir: "))
  if numero_conta >= 1 and numero_conta <= len(contas):
      conta = contas.pop(numero_conta - 1)
      print(f"\nA conta de {conta['nome']} foi excluída com sucesso!")
  else:
      print("Conta não encontrada. Certifique-se de que o número da conta é válido.")

def preferencias():
  numero_conta = int(input("Digite o número da conta que deseja acessar: "))

  pref = ['POO', 'EXERCICIO', 'INTRODUCAO', 'LOGICA', 'TESTES']
  if numero_conta >= 1 and numero_conta <= len(contas):
    conta = contas[numero_conta - 1]
    print("Bem-vindo de volta")
    while True:
      print("Opcôes: POO, Exercicios, introducao, logica, testes")
      escolha = input("Digite suas preferências uma a uma: ")
      escolha = escolha.upper()
      for escolha in pref:
        continua = input('Preferencia adicionada. Gostaria de adicionar mais uma? S/N ')
        continua = continua.upper()
        if continua == 'N':
          conta['preferencias'] = (escolha)
          return False
        elif continua == 'S':
          conta['preferencias'] = (escolha)
          break
        else:
          print('Preferencia não encontrada')
  else:
    print("Conta não encontrada. Certifique-se de que o número da conta é válido.")

while True:
  print("\nEscolha uma opção:")
  print("1. Cadastro")
  print("2. Exibir contas cadastradas")
  print("3. Editar cadastro")
  print("4. Excluir conta")
  print("5. Preferências")
  print("6. Sair")
    
  opcao = input("Digite o número da opção desejada: ")
    
  if opcao == '1':
    cadastro()
  elif opcao == '2':
    exibir_cadastro()
  elif opcao == '3':
    atualizar_cadastro()
  elif opcao == '4':
    excluir_conta()
  elif opcao == '5':
    preferencias()
  elif opcao == '6':
    break
  else:
    print("Opção inválida. Tente novamente.")
      