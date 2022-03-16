from typing import List
from time import sleep

from Models.Cliente import Cliente
from Models.Conta import Conta

contas: List[Conta] = []


def main() -> None:
    menu()


def menu() -> None:
    imprime_cabecalho()
    imprime_opcoes()

    pega_opcoes()


def imprime_cabecalho() -> None:
    print("======================================")
    print("=============== ATM ==================")
    print("=========== PYTHON BANK ==============")
    print("======================================")
    print()


def imprime_opcoes():
    print("Selecione uma opcao no menu:")
    print("1 - Criar conta")
    print("2 - Efetuar saque")
    print("3 - Efetuar deposito")
    print("4 - Efetuar tranferencia")
    print("5 - Listar contas")
    print("6 - Sair do sistema")
    print()


def pega_opcoes() -> None:
    opcao: int = int(input("Oque deseja fazer ? \n"))
    route_to_correct_action(opcao)


def route_to_correct_action(opcao: int = 1) -> None:
    if (opcao == 1):
        criar_conta()
    elif (opcao == 2):
        efetuar_saque()
    elif (opcao == 3):
        efetuar_deposito()
    elif (opcao == 4):
        efetuar_tranferencia()
    elif (opcao == 5):
        listar_contas()
    elif (opcao == 6):
        sair_do_sistame()
    else:
        mensagem_de_erro_para_opcao_invalida()


def criar_conta() -> None:
    print("Informe os dados do usuario abaixo:")

    nome: str = input("Nome: ")
    email: str = input("E-mail: ")
    cpf: str = input("CPF: ")
    data_nascimento: str = input("Data de nascimento: ")

    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso:")
    print("Dados da conta")
    print("-------------------")

    re_start_menu()


def efetuar_saque() -> None:
    if valida_numero_de_contas():
        numero: int = int(input("Informe o numero da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:  # verifica se existe conta
            valor: float = float(input("Quanto voce deseja sacar? "))
            conta.sacar(valor)
        else:
            print(f"Nao foi encontrada a conta com o numero: {numero}")
            re_start_menu()

    else:
        print("Ainda nao existem contas cadastradas!")
        re_start_menu()


def efetuar_deposito() -> None:
    if valida_numero_de_contas():
        numero: int = int(input("informe o numero da conta que vai depositar"))
        conta: Conta = buscar_conta_por_numero(numero)

        if conta:
            valor: float = float(input("Informe o valor que deseja depositar: "))
            conta.depositar(valor)

        else:
            print("Nao foi localizada nenhuma conta com o numero informado")
            re_start_menu()

    else:
        print("Ainda nao existem contas cadastradas")
        re_start_menu()


def efetuar_tranferencia() -> None:
    if valida_numero_de_contas(qtd=1):
        numero_origem: int = int(input("Informe o numero da sua conta: "))
        numero_destino: int = int(input("Informe o numero da conta de destino: "))

        conta_origem: Conta = buscar_conta_por_numero(numero_origem)
        conta_destino: Conta = buscar_conta_por_numero(numero_destino)

        if not conta_origem:
            print(f"Sua conta com número {conta_origem} nao foi encontrada...")
            re_start_menu()
            return

        if not conta_origem:
            print(f"A conta de destino com numero {conta_destino} nao foi encontrada...")
            re_start_menu()
            return

        valor: float = float(input("Diga o valor que deseja tranferir: "))
        conta_origem.transferir(conta_destino, valor)


    else:
        print("Ainda nao existem contas suficientes cadastradas")
        re_start_menu()


def listar_contas() -> None:
    if valida_numero_de_contas():
        print("Listagem de contas: ")
        for conta in contas:
            print(conta)
            sleep(1)
    else:
        print("nao existe contas cadastradas")
        re_start_menu()


def sair_do_sistame() -> None:
    print("Volte sempre")
    sleep(2)
    exit(0)


def mensagem_de_erro_para_opcao_invalida() -> None:
    print("A opçao selecionada é invalida, tente novamente !")
    re_start_menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    conta: Conta = None

    if valida_numero_de_contas():
        for conta in contas:
            if conta.numero == numero:
                c = conta

    return c


def re_start_menu() -> None:
    sleep(2)
    menu()


def valida_numero_de_contas(qtd: int = 0, cts: List[Conta] = contas) -> bool:
    eh_valido: bool = len(cts) > qtd
    return eh_valido


if (__name__ == '__main__'):
    main()
