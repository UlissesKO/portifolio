valorConta = 0
LIMITE = 500
numeroSaque = 0
saque = 0
opcao = 1
quantidadeSaques = 0
quantidadeDepositos = 0
users = {}

def sacar(valorSaque, valorConta, quantidadeSaques):#Só pode 3 saques diarios de no maximo 500, Registrado no extrato
    if quantidadeSaques <= 3:
        if valorConta >= valorSaque:
            valorConta -= valorSaque
            quantidadeSaques += 1
            print(f"Foram sacados R${valorSaque},00")
        else:
            print("Não tem saldo suficiente")
    else:
        print("Já estorou o limite")
    return valorConta, quantidadeSaques

def depositar(valorDeposito, valorConta, quantidadeDepositos):
    valorConta += valorDeposito
    quantidadeDepositos += 1
    print(f"Deposito de R%{valorDeposito},00 feito com sucesso")
    return valorConta, quantidadeDepositos

def vizualizar():
    print(f"Você possui R%{valorConta},00 na conta bancária\n Foram feitos {quantidadeSaques} saques e {quantidadeDepositos} depósitos")


while opcao != 1 or opcao != 2 or opcao != 3 or opcao != 0:
    opcao = input("Digite a operação desejada\n[1] Saque\n[2] Depósito\n[3] Extrato\n[0] Sair\n")
    match opcao:
        case "1":
            saque = int(input("Quanto deseja sacar?\n"))
            if saque > LIMITE or saque <= 0:
                print("O máximo é 500")
                saque = int(input("Quanto deseja sacar?\n"))
            else:
                sacar(saque, valorConta, quantidadeSaques)
        case "2":
            deposito = int(input("Quanto deseja depositar?\n"))
            depositar(saque, valorConta, quantidadeDepositos)
        case "3":
            vizualizar()
        case "0":
            break
        case _ :
            print("Digite uma opção válida")