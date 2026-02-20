from random import randint


class Conta:
    def __init__(self, titular: str):
        #Variáveis
        self.titular = str(titular)
        self.saldo = int(0.0)
        self.numero = randint(1000, 9999)

    #Métodos
    def depositar(self, val: float):
        self.saldo += val #Adicionando o depósito
        print('Valor adicionado a conta!') #Retornando confirmação
        
    def sacar(self, val: float):
        if self.saldo >= val: #Verificando se o valor na conta é suficiente
            self.saldo -= val #Retirando o valor da conta
            print('Valor sacado com sucesso!') #Confirmação
        else: print('Saldo insuficiente para transação!') #Mensagem de caso de erro

    def transferir(self, val: float, destino: "Conta"):
        if self.saldo >= val: #Verificando se a conta possui o valor da transferência
            self.sacar(val) #Retirando o valor da conta
            destino.depositar(val) #Adicionando o valor na outra conta
            print('Valor transferido com sucesso') #Confirmação
        else: print('Erro verifique se a conta possui valor o suficiente e se o destinatário existe') #Mensagem de erro

    def __str__(self): #Sobrescrever (override) #Esse comando sobrescreve a saída, quando printamos a variável, ao invés de um local da memória, será impresso os valores que colocamos
        return f"Titular = {self.titular}\nNúmero = {self.numero}\nSaldo = R$ {self.saldo}"

#Programa principal
conta = Conta('selmini')
conta2 = Conta('Carlos Rafael')
conta.depositar(7500)
conta.transferir(7000, conta2)
print(conta.saldo)
print(conta2.saldo)
print(conta)