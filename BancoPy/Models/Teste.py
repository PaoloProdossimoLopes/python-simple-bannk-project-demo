from Models.Cliente import Cliente
from Models.Conta import Conta

felicity: Cliente = Cliente("Felicity Jones", "fe@gmail.com", "000.000.000-0", "10/01/2000")
Paolo: Cliente = Cliente("Paolo Prodossimo Lopes", "pprodosismo@gmail.com", "000.000.000-0", "10/01/2000")
Leticia: Cliente = Cliente("Leticia O. Speda", "oliveiraS@gmail.com", "000.000.000-0", "10/01/2000")

conta1: Conta = Conta(Leticia)
conta2: Conta = Conta(Paolo)
