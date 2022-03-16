from Models.Cliente import Cliente
from Utils.Helper import formata_float_str_moeda


class Conta:
    codigo: int = 1001

    def __init__(self: object, cliente: Cliente):
        self.__numero: int = Conta.codigo
        self.__cliente: Cliente = cliente
        self.__saldo: float = 0.0
        self.__limite: float = 100.0
        self.__saldo_total: float = self._calcula_saldo_total
        Conta.codigo += 1

    def __str__(self: object) -> str:
        return f'Numero da conta: {self.numero}\n\
        Cliente: { self.cliente.nome }\n\
        Saldo total: { formata_float_str_moeda(self.saldo_total) }'

    @property
    def numero(self: object) -> int:
        return self.__numero

    @property
    def cliente(self: object) -> Cliente:
        return self.__cliente

    @property
    def saldo(self: object) -> float:
        return self.__saldo

    @saldo.setter
    def saldo(self: object, valor: float) -> None:
        self.__saldo = valor

    @property
    def limite(self: object) -> float:
        return self.__limite

    @limite.setter
    def limite(self: object, valor: float) -> None:
        self.__limite = valor

    @property
    def saldo_total(self: object) -> float:
        return self.__saldo_total

    @saldo_total.setter
    def saldo_total(self: object, valor: float) -> None:
        self.__saldo_total = valor

    @property
    def _calcula_saldo_total(self: object) -> float:
        return (self.saldo + self.limite)


    def depositar(self: object, valor: float) -> None:
        tem_dinheiro_suficiente: bool = (valor > self.saldo_total)
        valor_eh_valido: bool = (valor > 0)
        if tem_dinheiro_suficiente and valor_eh_valido:
            self.saldo = self.saldo + valor
            self.saldo_total = self._calcula_saldo_total
            print("Deposito realizado com sucesso")
        else:
            print("O valor de desposito é invalido")


    def sacar(self: object, valor: float) -> None:
        tem_dinheiro_suficiente: bool =  (valor > self.saldo_total)
        valor_eh_valido: bool = (valor > 0)
        if tem_dinheiro_suficiente and valor_eh_valido:
            if tem_dinheiro_suficiente and valor_eh_valido:
                if valor >= valor:
                    self.saldo = self.saldo + valor
                    self.saldo_total = self._calcula_saldo_total
                else:
                    restante: float = self.saldo - valor
                    self.limite = self.limite + restante
                    self.saldo = 0
                    self.saldo_total = self._calcula_saldo_total
            print("Saque realizado com sucesso")
        else:
            print("O valor de saque é indisponivel")


    def transferir(self: object, destino: object, valor: float) -> None:
        if valor > 0 and self.saldo_total >= valor:
            if self.saldo >= valor:
                self.saldo = self.saldo - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total
            else:
                restante: float = self.saldo - valor
                self.saldo = 0
                self.limite = self.limite - valor
                self.saldo_total = self._calcula_saldo_total
                destino.saldo = destino.saldo + valor
                destino.saldo_total = destino._calcula_saldo_total

            print("Tranferencia realizada com sucesso")
        else:
            print("Erro ao tentar tranferir ... ")
