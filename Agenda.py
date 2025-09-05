class Contacto:
    def __init__(self, nombre, telefono, email):
        self.nombre = nombre
        self.telefono = telefono
        self.email = email

    def __str__(self):
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"


class Agenda:
    def __init__(self):
        self.contactos = []

    def crear_contacto(self, nombre, telefono, email):
        nuevo_contacto = Contacto(nombre, telefono, email)
        self.contactos.append(nuevo_contacto)
        print("Contacto creado con éxito.")

    def actualizar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                print("Contacto encontrado. Ingresa los nuevos datos:")
                contacto.nombre = input("Nuevo nombre: ")
                contacto.telefono = input("Nuevo teléfono: ")
                contacto.email = input("Nuevo email: ")
                print("Contacto actualizado con éxito.")
                return
        print("Contacto no encontrado.")

    def eliminar_contacto(self, nombre):
        for contacto in self.contactos:
            if contacto.nombre == nombre:
                self.contactos.remove(contacto)
                print("Contacto eliminado con éxito.")
                return
        print("Contacto no encontrado.")

    def mostrar_contactos(self):
        if not self.contactos:
            print("La agenda está vacía.")
        else:
            print("Contactos en la agenda:")
            for contacto in self.contactos:
                print(contacto)


def menu():
    agenda = Agenda()
    while True:
        print("\n--- Menú de Agenda ---")
        print("1. Crear un contacto")
        print("2. Actualizar un contacto")
        print("3. Eliminar un contacto")
        print("4. Mostrar todos los contactos")
        print("5. Salir")
        
        try:
            opcion = int(input("Selecciona una opción (1-5): "))
            if opcion == 1:
                nombre = input("Nombre: ")
                telefono = input("Teléfono: ")
                email = input("Email: ")
                agenda.crear_contacto(nombre, telefono, email)
            elif opcion == 2:
                nombre = input("Nombre del contacto a actualizar: ")
                agenda.actualizar_contacto(nombre)
            elif opcion == 3:
                nombre = input("Nombre del contacto a eliminar: ")
                agenda.eliminar_contacto(nombre)
            elif opcion == 4:
                agenda.mostrar_contactos()
            elif opcion == 5:
                print("Saliendo de la agenda...")
                break
            else:
                print("Opción inválida. Por favor, selecciona un número del 1 al 5.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número del 1 al 5.")


# Llamada al menú principal
if __name__ == "__main__":
    menu()