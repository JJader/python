from classes.celula import Cell
from classes.lista import Lista
import os


def cabecario():
    print("1 --> adicionar no final")
    print("2 --> adicionar no index")
    print("3 --> remover")
    print("4 --> pesquisar item")
    print("5 --> pesquisar posição")
    print("6 --> modificar")
    print("7 --> imprimir")
    print("8 --> sair")


def main():
    l1 = Lista()
    op = 0
    while(op != 8):
        cabecario()
        try:
            op = int(input("Digite a opção desejada: "))
            if op == 1:
                item = float(input("Digite o valor do item: "))
                l1.append(item)
            if op == 2:
                item = float(input("Digite o valor do item: "))
                index = int(input("Digite o valor do index: "))
                l1.insert(index, item)
            if op == 3:
                item = float(input("Digite o valor do item: "))
                l1.pop(item)
            if op == 4:
                item = float(input("Digite o valor do item: "))
                print(l1.search(item))
            if op == 5:
                index = int(input("Digite o valor do index: "))
                print(l1[index])
            if op == 6:
                item = float(input("Digite o valor do item: "))
                index = int(input("Digite o valor do index: "))
                l1[index] = item
            if op == 7:
                print(l1)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()
