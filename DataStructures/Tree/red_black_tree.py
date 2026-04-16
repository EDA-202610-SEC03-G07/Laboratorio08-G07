import rbt_node as rbt




def new_rbt():
    return {
        "root": None,
        "type": "RBT",
    }
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
def size(my_tree):
    if my_tree is None:
        return 0
    return size_tree(my_tree["root"])

def size_tree(my_node):
    if my_node is None:
        return 0
    else:
        return 1 + size_tree(my_node["left"]) + size_tree(my_node["right"])

def rotate_left(node_rbt):
    #El nodo derecho del nodo a rotar se convierte en el nuevo nodo raiz,
    # el nodo a rotar se convierte en el hijo izquierdo del nuevo nodo raiz y 
    # el hijo izquierdo del nuevo nodo raiz se convierte en el hijo derecho del nodo a rotar
    new_root = node_rbt["right"]
    node_rbt["right"] = new_root["left"]
    new_root["left"] = node_rbt
    new_root["color"], node_rbt["color"] = node_rbt["color"], new_root["color"]
    return new_root

def rotate_right(node_rbt):
    #El nodo izquierdo del nodo a rotar se convierte en el nuevo nodo raiz,
    # el nodo a rotar se convierte en el hijo derecho del nuevo nodo raiz y 
    # el hijo derecho del nuevo nodo raiz se convierte en el hijo izquierdo del nodo a rotar
    new_root = node_rbt["left"]
    node_rbt["left"] = new_root["right"]
    new_root["right"] = node_rbt
    new_root["color"], node_rbt["color"] = node_rbt["color"], new_root["color"]
    return new_root

#Funcion de comparacion de nodos

def default_compare(key, element):
    """
    Compara key con la llave del elemento (element es un nodo dict).
    Retorna:
      0  si key == element.key
      1  si key > element.key
     -1  si key < element.key
    """
    if element is None:
        return -1
    node_key = rbt.get_key(element)
    if node_key is None:
        return -1
    if key == node_key:
        return 0
    if key > node_key:
        return 1
    return -1
def flip_node_color(node_rbt):
    #Cambia el color del nodo a rojo y el color de sus  hijos
    if rbt.is_red(node_rbt):
        node_rbt["color"] = "BLACK"
    else:
        node_rbt["color"] = "RED"