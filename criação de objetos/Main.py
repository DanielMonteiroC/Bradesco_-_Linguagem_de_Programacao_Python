class Main:
    pass

print("Testando o projeto")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("João", "114444-2222")
conta = Conta(c1._nome,6565,0)

print(conta._titular, " Numero: ",conta._numero, "Seu Saldo: ", conta._saldo)