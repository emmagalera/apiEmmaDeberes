from flask import Flask, jsonify, request

app= Flask(__name__)

# GET --> para hacer consultas. Envia informacion haciendola visible en la URL de la pagina web
# POST --> para crear . Envia informacion ocultandola del usuario
# PUT --> para modificar 
# DELETE --> para eliminar 

from productosTienda import productos


@app.route("/")
def todosLosAlimentos():
    return jsonify(productos)


@app.route('/<string:producto_categoria>')
def categorias(producto_categoria):
    
    resultado= [producto for producto in productos if (producto['categoria'] == producto_categoria)]
    if(len(resultado))>0:
        return jsonify({"resultado": resultado})
    else:
        return jsonify({"Mensaje":"Producto no encontrada"})

@app.route('/productos/<string:producto_nombre>')
def nombre(producto_nombre):
    resultado= [producto for producto in productos if (producto['nombre'] == producto_nombre)]
    if(len(resultado))>0:
        return jsonify({"resultado": resultado})
    else:
        return jsonify({"Mensaje":"Producto no encontrada"})

@app.route('/productos/', methods=['POST'])
def anadirProducto():
    nuevoProducto= {
        "nombre": request.json['nombre'],
        "categoria": request.json['categoria'],
        "precio": request.json['precio'],
        "stock": request.json['stock']
    }
    productos.append(nuevoProducto)
    return jsonify({"Mensaje": "Producto añadido", "resultado": productos})

@app.route('/productos/<string:producto_nombre>', methods=['PUT'])
def modificarProducto(producto_nombre):
    resultado= [producto for producto in productos if (producto['nombre'] == producto_nombre)]
    if(len(resultado)>0):
        resultado[0]['nombre']= request.json['nombre']
        resultado[0]['categoria']= request.json['categoria']
        resultado[0]['precio']= request.json['precio']
        resultado[0]['stock']= request.json['stock']
        return jsonify({"Mensaje": "Producto modificado", "resultado": productos})


@app.route('/productos/<string:producto_nombre>', methods=['DELETE'])
def borrarProducto(producto_nombre):
    resultado= [producto for producto in productos if (producto['nombre'] == producto_nombre)]
    if(len(resultado)>0):
        productos.remove(resultado)
        return jsonify({"Mensaje": "Producto Eliminado", "resultado": productos})


if __name__ == '__main__':
    app.run(debug=True, port=2000)