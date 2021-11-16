import persistencia_json

lista = []
while True:
    marcacoche = input("Marca Coche: ")
    if marcacoche == "fin":
        break
    modelocoche = input("Modelo de Coche: ")
    combustible = input("Combustible: ")
    cilindrada = input("Cilindrada: ")
    datos = {}
    datos ["marcacoche"] = marcacoche
    datos ["modelocoche"] = modelocoche
    datos ["combustible"] = combustible
    datos ["cilindrada"] = cilindrada
    lista.append(datos)
persistencia_json.store(lista, "coches.txt")
lista = []
lista = persistencia_json.retrieve("coches.txt")
print("Lista Coches: \n",lista)