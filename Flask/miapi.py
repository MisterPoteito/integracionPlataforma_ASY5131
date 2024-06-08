from flask import Flask, request

app = Flask(__name__)

## APP de Prueba para API Cliente
listaDelivery = []
listaCliente = []
listaProducto = []

@app.get("/cliente")
def getClientes():
    return listaCliente

@app.get("/cliente/<id>")
def getCliente(id):
    return listaCliente.index(id)

@app.post("/cliente")
def insertaCliente():
    json = request.get_json()
    
    cliente = {
        "id": json["id"],
        "razonSocial": json["razonSocial"],
        "rut": json["rut"],
        "direccion": json["direccion"] 
    }
    print(cliente)

    listaCliente.append(cliente)
    return "Cliente Creado"

@app.put("/cliente/<id>")
def actualizaCliente(id):
    index = int(id)
    json = request.get_json()

    cliente = {
        "id": json["id"],
        "razonSocial": json["razonSocial"],
        "rut": json["rut"],
        "direccion": json["direccion"] 
    }

    if listaCliente and 0 <= index < len(listaCliente):
        listaCliente.pop(index)
        listaCliente.append(cliente)
        return "Cliente Actualizado"
    else:
        return "Error al actualizar: lista vacía o índice inválido", 400

@app.delete("/cliente")
def borrarClientes():
    listaCliente.clear()
    return "Clientes Borrados"

@app.delete("/cliente/<id>")
def borrarCliente(id):
    index = int(id) - 1
    listaCliente.pop(index)
    return "Cliente " + id +  " Borrado"


### Aquí inicia Producto


@app.get("/producto")
def getProductos():
    return listaProducto

@app.get("/producto/<id>")
def getProducto(id):
    return listaProducto.index(id)

@app.post("/producto")
def insertaProducto():
    json = request.get_json()
    
    producto = {
        "id": json["id"],
        "nombre": json["nombre"],
        "categoria": json["categoria"],
        "descripcion": json["descripcion"] 
    }
    print(producto)

    listaProducto.append(producto)
    return "Producto Creado"

@app.put("/producto/<id>")
def actualizaProducto(id):
    index = int(id)
    json = request.get_json()
    
    producto = {
        "id": json["id"],
        "nombre": json["nombre"],
        "categoria": json["categoria"],
        "descripcion": json["descripcion"] 
    }
    listaProducto.pop(index)
    listaProducto.append(producto)

    return "Producto Actualizado"

@app.delete("/producto")
def borrarProductos():
    listaProducto.clear()
    return "Productos Borrados"

@app.delete("/producto/<id>")
def borrarProducto(id):
    index = int(id) - 1
    listaProducto.pop(index)
    return "Producto " + id +  " Borrado"



### Aquí inicia Delivery
@app.get("/delivery")
def getDeliveries():
    return listaDelivery

@app.get("/delivery/<id>")
def getDelivery(id):
    for index, delivery in enumerate(listaDelivery):
        if delivery["id"] == int(id):
            return delivery
    return "Delivery not found", 404

@app.post("/delivery")
def insertDelivery():
    json = request.get_json()

    delivery = {
        "id": json["id"],
        "estado": json["estado"],
        "productos": json["productos"]
    }

    listaDelivery.append(delivery)
    return "Delivery created"

@app.put("/delivery/<id>")
def updateDelivery(id):
    json = request.get_json()

    for index, delivery in enumerate(listaDelivery):
        if delivery["id"] == int(id):
            listaDelivery[index] = {
                "id": json["id"],
                "estado": json["estado"],
                "productos": json["productos"]
            }
            return "Delivery updated"
    return "Delivery not found", 404

@app.delete("/delivery")
def deleteDeliveries():
    listaDelivery.clear()
    return "Deliveries deleted"

@app.delete("/delivery/<id>")
def deleteDelivery(id):
    for index, delivery in enumerate(listaDelivery):
        if delivery["id"] == int(id):
            listaDelivery.pop(index)
            return f"Delivery {id} deleted"
    return "Delivery not found", 404

if __name__ == "__main__":
    app.run(debug=True)