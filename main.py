from avl import *

myTree = AVL_Tree(3)
root = None
option = 0
while(option != 8):
    print("1.\tInserir dado")
    print("2.\tRemover dado")
    print("3.\tBuscar dado")
    print("4.\tExibir árvore")
    print("5.\tSalvar árvore")
    print("6.\tCarregar árvore")
    print("7.\tInserir planilha")
    print("8.\tSair")

    option = int(input())
    if(option == 1):
        print("CEP:", end=" ")
        zipcode = int(input())

        print("Rua:", end=" ")
        street = input()

        print("Bairro:", end=" ")
        nbhd = input()
        s = Street(zipcode, street, nbhd)
        root = myTree.insert(root, s)
    elif(option == 2):
        print("CEP:", end=" ")
        zipcode = int(input())
        root = myTree.delete(root, zipcode)

    elif(option == 3):
        print("CEP:", end=" ")
        zipcode = int(input())
        street = myTree.search(root, zipcode)
        
    elif(option == 4):
        myTree.preOrder(root)

    elif(option == 5):
        myTree.mountFile(root)
        myTree.saveFile()
        print("Arquivo salvo!")
    
    elif(option == 6):
        streets = myTree.rebuildTree("tree.txt")
        for s in streets:
            root = myTree.insert(root, s)
    
    elif(option == 7):
        print("Nome do aqruivo: ", end=" ")
        filename = input();
        base = open(filename, "r")

        data = base.read().split("\n")
        for d in data:
            input_street = d.split(",")
            if d != '':
                street = Street(int(input_street[0]), input_street[1], input_street[2])
                root = myTree.insert(root, street)
        print("Dados inseridos com sucesso!")