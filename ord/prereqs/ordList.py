class Node:
    def __init__(self, data = None):
        self.next = None
        self.data = data

class List:
    def __init__(self):
        self.node = Node()
        self.size = 0
        self.head = self.node
        print('criou')

    def printList(self):
        if aux is not None:
            print(aux.data)
            aux = aux.next

        return self.printList()


        # while aux is not None:
        #     print(aux.data)
        #     aux = aux.next

        # if not aux.next:
        #     print(self.node.data)
        #     print('next F')
        # else:
        #     print('next T')
        #     aux.next.printList()

    def tamanho(self):
        print(self.size)

    def insert(self, data):
        if self.node.data:
            if self.node.next is None:
                self.node.next = Node(data)
                self.size += 1
                print('inser 1.1')
        else:
            self.node.data = data
            self.size += 1
            print('inser 2')


if __name__ == "__main__":
    lista = List()
    lista.insert(1)
    lista.insert(2)
    lista.tamanho()
    lista.printList()
