from conta import Contas

conta_nova = Contas()
conta_nova.numero = 123
conta_nova.cliente = 'Guilherme'
conta_nova.limite = 100

conta_nova.imprimirSaldo()

conta_nova.depositar(50)

conta_nova.imprimirSaldo()