"""""
# Crear una instancia de SList
my_list = SList()

# Agregar elementos al frente
my_list.add_to_front(3)
my_list.add_to_front(2)
my_list.add_to_front(1)

# Imprimir los valores de la lista
my_list.print_values()
# Salida esperada: 1 2 3

# Agregar elementos al final
my_list.add_to_back(4)
my_list.add_to_back(5)

# Imprimir los valores de la lista
my_list.print_values()
# Salida esperada: 1 2 3 4 5

# Remover el primer elemento
my_list.remove_from_front()

# Imprimir los valores de la lista
my_list.print_values()
# Salida esperada: 2 3 4 5

# Remover el último elemento
my_list.remove_from_back()

# Imprimir los valores de la lista
my_list.print_values()
# Salida esperada: 2 3 4

# Remover un valor específico
my_list.remove_val(3)

# Imprimir los valores de la lista
my_list.print_values()
# Salida esperada: 2 4

# Insertar un valor en una posición específica
my_list.insert_at(3, 1)

# Imprimir los valores de la lista
my_list.print_values()
# Salida esperada: 2 3 4

"""""


class SList:
    def __init__(self):
        self.head = None

    def add_to_front(self, val):
        new_node = SLNode(val)
        current_head = self.head
        new_node.next = current_head
        self.head = new_node
        return self

    def print_values(self):
        runner = self.head
        while runner:
            print(runner.value)
            runner = runner.next
        return self

    def add_to_back(self, val):
        if not self.head:
            self.add_to_front(val)
            return self

        new_node = SLNode(val)
        runner = self.head
        while runner.next:
            runner = runner.next
        runner.next = new_node
        return self

    def remove_from_front(self):
        if not self.head:
            return None

        removed_value = self.head.value
        self.head = self.head.next
        return removed_value

    def remove_from_back(self):
        if not self.head:
            return None

        if not self.head.next:
            return self.remove_from_front()

        runner = self.head
        while runner.next.next:
            runner = runner.next
        removed_value = runner.next.value
        runner.next = None
        return removed_value

    def remove_val(self, val):
        if not self.head:
            return None

        if self.head.value == val:
            return self.remove_from_front()

        runner = self.head
        while runner.next:
            if runner.next.value == val:
                removed_value = runner.next.value
                runner.next = runner.next.next
                return removed_value
            runner = runner.next

        return None

    def insert_at(self, val, n):
        if n == 0:
            return self.add_to_front(val)
        
        new_node = SLNode(val)
        runner = self.head
        count = 0
        while runner:
            if count == n - 1:
                new_node.next = runner.next
                runner.next = new_node
                return self
            runner = runner.next
            count += 1

        return None

class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None

