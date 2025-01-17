from clientes import Cliente
from bancos import Banco
from contas import Conta, ContaEspecial
glinda = Cliente("Glinda da Terra mais ao Norte", "789-5642")
elphaba = Cliente("Bruxa má do oeste", "156-4895")
fiyero = Cliente("Príncipe Fiyero", "149-7569")
contaEG = Conta([elphaba, glinda], 1, 3000)
contaF = ContaEspecial([fiyero], 2)
shiz = Banco("Shiz")
shiz.abre_conta(contaEG)
shiz.abre_conta(contaF)
shiz.lista_contas()
contaEG.saque(800)
contaEG.deposito(200)
contaEG.saque(500)
contaF.deposito(149)
contaF.saque(50)
contaEG.extrato()
contaF.extrato()