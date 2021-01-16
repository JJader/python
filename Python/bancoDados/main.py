from banco_de_dados import Banco_de_dados
import os
os.system("clear")


bd = Banco_de_dados()
bd.inserir_clientes(1, 'jamisson')
bd.inserir_clientes(2, 'Mary')
bd.inserir_clientes(3, 'João')
bd.excluir_cliente(0)

bd.imprimir_clientes()

print(bd.nome)
bd.nome = "jamisson"
print(bd.nome)