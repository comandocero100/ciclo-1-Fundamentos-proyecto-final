lista = []
op = 0
letra = ""


def mostrar(lista):
    print("Listado de beneficiarios:")
    for i in lista:
        print(i)


def busq(lista):
    fuera = []
    letra = str(input("Digite la letra por la que empiezan los beneficiarios:\n"))
    for i in range(0, len(lista)):
        if i == 0 or (i % 3) == 0:
            if str((lista[i][:1])).lower() == letra.lower():
                fuera.append(lista[i])
                fuera.append(lista[i+1])
                fuera.append(lista[i+2])
    print("Listado filtrado de beneficiarios:")
    return fuera


def busq2(lista):
    nombre = str(input("Digite el nombre y apellido del beneficiario a buscar:\n"))
    for i in range(0,len(lista)):
        if i == 0 or (i % 3)==0:
            if str(lista[i]).lower() == nombre.lower():
                return print(f"{lista[i]}\n{lista[i+1]}\n{lista[i+2]}")
    return print("No se encuentra ningun beneficiario registrado")


def elimin(lista):
    cc = input("Digite la cedula del beneficiario a borrar:\n")
    indice = 1
    if cc in lista:
        for elemento in range(0, len(lista), 3):
            if lista[indice] == cc:
                lista.pop(indice + 1)
                lista.pop(indice)
                lista.pop(indice - 1)
                return "El usuario ha sido eliminado del listado"
            indice += 3
    else:
        return "No se encontró el usuario"


while op != 6:
    print("Menu principal\n1. Ver listado\n2. Ver listado filtrado\n3. Agregar beneficiario\n4. Buscar beneficiario\n5. Borrar beneficiario\n6. Salir")
    op = int(input())
    if op == 1:
        mostrar(lista)
    elif op == 2:
        for i in busq(lista):
            print(i)
    elif op == 3:
        if len(lista) <= 10:
            print("Digite la información del beneficiario a agregar:")
            nombre=str(input())
            cedula=str(input())
            celular=str(input())
            lista.append(nombre)
            lista.append(cedula)
            lista.append(celular)
            print("El beneficiario ha sido agregado")
    elif op == 4:
        busq2(lista)
    elif op == 5:
        print(elimin(lista))
    elif op == 6:
        print("Hasta pronto")
# Grabar archivo
archivo = open('agenda.txt','w',encoding='utf8')
for elemento in lista:
    archivo.write(str(elemento)+"\n")
archivo.close()
