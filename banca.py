import textwrap

def menu():
    menu = """\n

    ================== MENU =================

    [d]\tDeposito
    [l]\tLevantar
    [c]\tNovo Cliente
    [nc]\tNova Conta
    [lc]\tListar Contas
    [e]\tExtrato
    [s]\tSair

    => """
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f'Deposito:\tAOA {valor:.2f}\n'
        print('\n=== Deposito realizado com sucesso! ===')
    else:
        print('@@@ Operacao falhou! O valor informado e invalido. @@@')
    
    return saldo, extrato


def saque(saldo, valor, extrato, limite, num_saques, limite_saque):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saque = num_saques >= limite_saque

    if excedeu_saldo:
        print('n\@@@ Operacao Falhou! Saldo insuficiente. @@@')
    
    elif excedeu_limite:
        print('@@@ Operacao falhou. Excedeu o limite. @@@')
    
    elif excedeu_saque:
        print('\t@@@ Operacao falhou. Atingiu o limite maxima de levantamento. @@@')
    
    elif valor > 0:
        saldo -= valor
        extrato += f'\n levantamento:\t AOA {valor:.2f}\n'
        num_saques += 1
        print('\n@@@ Levantamento realizado com sucesso. @@@')

    else:
        print('@@@ Operacao falhou. Valor invalido. @@@')

    return saldo, extrato


def ver_extrato(saldo, extrato):
            print("===============EXTRATO==========================")
            print('Sem movimentacoes.' if not extrato else extrato)
            print(f'\nSaldo: \tAOA {saldo:.2f}')
            print('=================================================')

def criar_cliente(clientes):
    bi = input('Informe o seu BI: ')
    cliente = filtrar_cliente(bi, clientes)

    if cliente:
        print('\n@@@ Cliente com este BI, ja registado. @@@')
        return

    nome = input('Inform o seu nome completo: ')
    data_nascimento = input('Informe a sua data de nascimento(dd-mm-aaaa): ')
    endereco = input('Informe o seu endereco (cazenga, nro - bairro - cidade): ')

    clientes.append({'nome': nome, 'data_nascimento': data_nascimento, 'bi': bi, 'endereco': endereco})

    print('=== Cliente criado com sucesso. ===')


def filtrar_cliente(bi, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente['bi'] == bi]
    return clientes_filtrados[0] if clientes_filtrados else None



def criar_conta(agencia, numero_conta, clientes, contas):
    bi = input('Informe o BI do cliente: ')
    cliente = filtrar_cliente(bi, clientes)

    if cliente:
        print('\n=== Conta criada com sucesso! ===')
        conta = {'agencia': agencia, 'numero_conta': numero_conta, 'cliente': cliente}
        contas.append(conta)
        return conta

    print('\n@@@ Cliente nao encontrado, fluxo de criacao da conta encerrado! @@@')


def listar_contas(contas):
    for conta in contas:
        linha = f"""
            Agencia: \n{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['cliente']['nome']}
        
        """
        print('=' * 100)
        print(textwrap.dedent(linha))

def main():
    LIMITE_SAQUE = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 1000
    extrato = ""
    num_saques = 0
    clientes = []
    contas = []
   

    while True:

        opcao = menu()

        if opcao == 'd':
            valor = float(input('Informa o valor a depositar: '))

            saldo, extrato = depositar(saldo, valor, extrato)
            
        
        elif opcao == 'l':
            valor = float(input('Informa o valor a levantar: '))

            saldo, extrato = saque(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                limite = limite,
                num_saques = num_saques,
                limite_saque= LIMITE_SAQUE,
            )

        elif opcao == 'e':
            ver_extrato(saldo, extrato)

        elif opcao == 'c':
            criar_cliente(clientes)

        elif opcao == 'nc':
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, clientes, contas)

            if conta:
                contas.append(conta)


        elif opcao == 'lc':
            listar_contas(contas)


        elif opcao == 's':
            break

        else:
            print('Falha na operacao. Selecione uma operacao valida.')

main()
