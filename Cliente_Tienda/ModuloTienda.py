from ModuloCliente import Cliente

class Tienda:
    def __int__(self, inventario):
        self.inventario = inventario

    def realizar_compra(self, Cliente1):
        categoria = Cliente1.categoria_favorita
        if categoria in self.inventario and len[self.inventario[categoria]] > 0:
            producto_comprado = self.inventario[categoria].pop(0)
            print(f"el cliente {Cliente1.nombre} ha comprado un/a {producto_comprado}.")
        else:
            print(F"lo sentimos, {Cliente1.nombre}, no tenemos el producto")

    def __str__(self):
        return f"Inventario de la tienda: {self.inventario}"


Cliente1 = ("Federico", "Calle  570", "federico@email.com", "tecnologia,")

inventario = {
    "tecnologia": ["celular", "notebook", "TV"],
    "moda": ["pantalones", "remeras", "vestidos"]
}

