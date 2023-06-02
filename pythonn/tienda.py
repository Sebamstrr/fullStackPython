class Tienda:
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []

    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)

    def vender_producto(self, id):
        if id < len(self.productos):
            producto = self.productos.pop(id)
            producto.print_info()
        else:
            print("No se encontró el producto con el ID proporcionado.")

    def inflacion(self, porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento, True)

    def hacer_liquidacion(self, categoria, porcentaje_descuento):
        for producto in self.productos:
            if producto.categoria == categoria:
                producto.actualizar_precio(porcentaje_descuento, False)


class Producto:
    def __init__(self, nombre, precio, categoria):
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria

    def actualizar_precio(self, cambio_porcentaje, esta_elevado):
        if esta_elevado:
            self.precio *= (1 + cambio_porcentaje / 100)
        else:
            self.precio *= (1 - cambio_porcentaje / 100)

    def print_info(self):
        print(f"Nombre: {self.nombre}")
        print(f"Categoría: {self.categoria}")
        print(f"Precio: ${self.precio}")


# Prueba de las clases
tienda = Tienda("Mi Tienda")

producto1 = Producto("Producto 1", 10.0, "Categoría A")
producto2 = Producto("Producto 2", 20.0, "Categoría B")
producto3 = Producto("Producto 3", 30.0, "Categoría A")

tienda.agregar_producto(producto1)
tienda.agregar_producto(producto2)
tienda.agregar_producto(producto3)

tienda.vender_producto(1)

producto4 = Producto("Producto 4", 40.0, "Categoría C")
tienda.agregar_producto(producto4)

tienda.inflacion(10)
tienda.hacer_liquidacion("Categoría A", 20)

print("---- Productos en la tienda ----")
for producto in tienda.productos:
    producto.print_info()
    print()

