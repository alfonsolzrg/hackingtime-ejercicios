Estructuras de datos basicas

Operaciones:
- Agregar un elemento nuevo
- Quitar un elemento
- Actualizar un elemento
- Obtener un elemento

1. Arreglo
 - El acceso a los elementos es por medio de un indice
 - Su tama;o se especifica al inicializarlo
 - El acceso a un elemento toma un tiempo constante (no importa si su indice es 1 o 100)

```
Declarando un arreglo en C
int *a = [200] -> 200 es el tama;o, y contiene elementos de tipo int
```

2. Lista ligada
Consiste en una coleccion de nodos, donde cada nodo tiene:
  - Los datos a guardar
  - Link al siguiente nodo de la lista ligada
- Puede guardar N cantidad de datos (limite es la memoria de la compu)
- El tiempo de acceso a los datos es variable y depende de la longitud de la lista
- Siempre mantenemos una referencia (una variable apuntando) a la raiz de la lista (el primer nodo)

```
class LinkedList():
  self.root = None

  def init(root_data):
    self.root = Node(data=root_data, next = None)

  def getNode(data):
    tmp = self.root
    if tmp.data == data:
      return tmp
    while tmp.next is not None:
      tmp = tmp.next
      if tmp.data == data:
        return tmp
    return None

  def addNodeAtStart(data):
    new_node = Node(data=data, next = self.root)
    self.root = new_node

  def addNodeAtEnd(data):
    tmp = self.root
    while tmp.next is not None:
      tmp = tmp.next
    # aqui ya estamos seguros de que estamos al final de la lista porque no hay
    # un siguiente nodo
    new_node = Node(data=data, next=None)
    tmp.next = new_node

##Tarea colaboration : D

def deleteNode(data):
  ##First node to delete
  tmp = self.root
  if tmp.data == data:
    self.root = tmp.next
  ##Each other node
    while tmp.next is not None:
      prevNode = tmp
      tmp = tmp.next
      if tmp.data == data:
        prevNode.next = tmp.next
    return None
​
​
  def addNodeBetweenTwoNodes(left, right, data):

    tmp = self.root
    while tmp.next is not None:
      if tmp.data == left:
        nextNode = tmp.next
        if nextNode.data == right: 
          nodeBetween.data = data
          nodeBetween.next = nextNode
          tmp.next = nodeBetween
          return tmp
    return None


    

    


    



  def updateNode(new_data):
    node = self.getNode(data)
    node.data = new_data


class Node():
  self.__init__(data, next=None)
    self.data = data
    self.next = next
  
node_data = 'alfonso'.split('') # -> ['a', 'l',...]
ll = LinkedList(node_data[0])
for node_data in node_data[1:]:
  ll.addNodeAtEnd(node_data)
