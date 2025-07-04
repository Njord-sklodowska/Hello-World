class Agenda():
    def __init__(self):
        self.crear_contact = []
    
    def menu(self):    
        while True:
            print("que deseas hacer? \n")
            option = int(input("1. Crear contacto || 2. Eliminar Contacto || 3. Editar Contacto || 4. Lista Contacto || 5. Buscar Contacto || 6. Cerrar Agenda \n"))
            if  option == 1:
                self.name = input("crea nombre de contacto \n")
                self.phone = input("ingresa numero de telefono \n")
                self.mail = input("ingresa correo electronico \n")
                contact = {"name" : self.name , "phone": self.phone, "e-mail": self.mail}
                self.crear_contact.append(contact)
                print("contacto registrado!!!!")
            #esto es para eliminar cuando me peleo con un contacto
            elif option == 2:
                name = input("ingresa el contacto a borrar \n")
                for contact in self.crear_contact:
                    if contact ["name"].lower() == name.lower():
                        self.crear_contact.remove(contact)
                        print("contacto eliminado")        
                print("contacto no encontrado")

            elif option == 3:
                name = input("ingresa el contacto a editar \n")
                for contact in self.crear_contact:
                    if contact["name"].lower() == name.lower():
                        new_name = input("ingresa nuevo nombre")
                        new_phone = input("ingresa nuevo numero de telefono")
                        new_email = input("ingresa nuevo e-mail")
                        contact["name"] = new_name
                        contact["phone"] = new_phone
                        contact["e-mail"] = new_email
                        print("contacto actualizado")           
                print("contacto no encontrado!")
            
            elif option == 4:
                if not self.crear_contact:
                    print("contacto vacio!!")
                else:
                    print("lista de contactos: \n")
                    for i ,c in enumerate(self.crear_contact , start = 1):
                        print(f"{i} . {c['name']} - {c['phone']} - {c['e-mail']}")

            elif option == 5:
                buscar_contacto = input("nombre de contacto para busqueda")
                encontrado = []
                for contact in self.crear_contact:
                    if buscar_contacto.lower() in contact["name"].lower():
                        encontrado.append(contact)
                if encontrado:
                    print("se encontro contacto")
                    for i ,c in enumerate(encontrado , start =1):
                        print(f"{i} . {c['name']} - {c['phone']} - {c['e-mail']}")
                else:
                    print("no se encontro contacto")

            elif option == 6:
                print ("cerrando agenda, Adios!!")
                break

my_agenda = Agenda()
my_agenda.menu()