class Cliente:
    def __int__(self, nombre,  domicilio, email, categoria_favorita):
        self.nombre = nombre
        self.direccion = domicilio
        self.email = email
        self.categoria_favorita = categoria_favorita

    def actualizar_categoria(self, nueva_categoria):
        self.categoria_favorita = nueva_categoria
        print(f"Se cambio de categoria favorita de {self.nombre} es {self.categoria_favorita}")

    def __str__(self):
        return f"cliente{self.nombre}, direccion: {self.direccion}, email: {self.email}, categoria favorita {self.categoria_favorita}"


Cliente1 = ("Federico", "Calle  570", "federico@email.com", "tecnologia,")
Cliente2 = ("Sabrina", "Calle Coder 47785", "sabrina@email.com", "moda")
Cliente3 = ("Carolina", "Avenida 9 de julio 200", "carolina@email.com", "libros")
Cliente4 = ("Fernando", "Calle Programador 304", "Fernando@emial.com", "autos")

