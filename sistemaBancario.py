import datetime

transacoes = []
saques = 0
saldo = 0
saquesDiarios = 0


def sacar(valorSaque):
    global saldo
    global saquesDiarios

    if valorSaque > 500:
        print('Valor para saque não pode ser superior a R$500,00, retornando ao menu principal!')
        return

    if valorSaque <= 0:
        print('Valor para saque não pode ser 0 ou negativo, retornando ao menu principal!')
        return

    if saquesDiarios >= 3:
        print('Você excedeu a quantidade máxima de saques diário, retornando ao menu principal!')
        return

    if saldo < valorSaque:
        print(f'Você não tem saldo suficiente para realizar o saque, seu saldo é R${saldo:.2f}, retornando ao menu principal!')
        return

    novoSaque = {"data": datetime.datetime.today(), "descrição": "Saque", "valor": valorSaque }
    transacoes.append(novoSaque)
    saquesDiarios += 1
    saldo -= valorSaque
    print(f"Sacando --> R${valorSaque:.2f}")

def depositar(valorDeposito):
    if valorDeposito <= 0:
        print('Valor para depósito não pode ser 0 ou negativo, retornando ao menu principal!')
        return
      
    novoDeposito = {"data": datetime.datetime.today(), "descrição": "Depósito", "valor": valorDeposito }
    transacoes.append(novoDeposito)
    global saldo 
    saldo += valorDeposito
    print(f'Valor depositado com sucesso, seu novo saldo é: R${saldo:.2f}')

def visualizarExtrato():
    titulo = "SEU EXTRATO"
    print('-'*48)
    print(titulo.center(48,' '))
    print('-'*48)
    if len(transacoes) == 0:
        print("Não foram realizadas movimentações")
    else:
        for item in transacoes:
            data = f' {item["data"].strftime("%d-%m-%Y %H:%M:%S")}'
            tipoMovimentacao = f' {item["descrição"]}'
            valor = f' R${item["valor"]:.2f}'
            print('Data', data.rjust(48 - len('Data '), "."))
            print('Movimentação', tipoMovimentacao.rjust(48 - len('Movimentação '), "."))
            print('Valor', valor.rjust(48 - len('Valor '), "."))
            print()
    print(f' Saldo atual: R${saldo:.2f} '.center(48,'.'))
    
opcao = 0

while opcao != '4':
    print('-'*48)
    print('Bem vindo ao Seu Bank!'.center(48, ' '))
    print('-'*48)
    print('Selecione uma opção para informar ao nosso')
    print('sistema o que você deseja fazer em sua conta:')
    print('''
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Sair
    ''')
    print('-'*48)
    
    opcao = input()
    
    if not opcao.isnumeric():
        print('Opção inválida, por favor digite uma opção ente 1 e 4!')
        print()
        continue

    opcao = int(opcao)

    if opcao not in (1,2,3,4):
        print('Opção inválida, tente novamente!')
    
    
    if opcao == 1:
        try:
            valorSaque = float(input('Você escolheu a opção "Sacar", por favor informe o valor do saque:'))
            sacar(valorSaque)

        except ValueError:
            print('Valor para saque inválido, retornando ao menu principal!')
            continue
        
    if opcao == 2:
        try:
            valorDeposito = float(input('Você escolheu a opção "Depositar", por favor informe o valor do depósito:'))
            depositar(valorDeposito)
        
        except ValueError:
            print('Valor para depósito inválido, retornando ao menu principal!')
            continue

    if opcao == 3:
        visualizarExtrato()

    if opcao == 4:
        break

print('Finalizando sua sessão... O seu Bank agradece a preferência, volte sempre!')
print()