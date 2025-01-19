# Crie uma classe ContaBancaria com atributos como número da conta, titular e saldo.
# a) Adicione métodos para depósito, saque e exibição do saldo.
# b) Implemente uma lógica para impedir saques que excedam o saldo.

from decimal import Decimal


class ContaBancaria:
    
    def  __init__(self, numero_conta, titular, saldo):
        self.__numero_conta = numero_conta
        self.__titular = titular
        self.__saldo = Decimal(saldo)
    
    def depositar(self, valor):
        self.__saldo += Decimal(valor)
        return f"Saldo: R${self.__saldo:.2f}"
    
    def sacar(self, valor):
        if valor > self.__saldo:
            return "Saldo insuficiente."
        else:
            self.__saldo -= valor
            return f"Saldo: R${self.__saldo:.2f}"

    def exibir_saldo(self):
        return f"Saldo: R${self.__saldo:.2f}"
    

minha_conta = ContaBancaria("123456", "Nicolas Felipe", 500)

print(minha_conta.exibir_saldo())
print(minha_conta.depositar(100))
print(minha_conta.sacar(601))