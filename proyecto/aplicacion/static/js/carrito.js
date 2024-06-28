
let carrito = [];

function agregarAlCarrito(productoId) {
    // Encuentra el precio del producto basado en su ID
    let precio = obtenerPrecio(productoId);
    
    // Agrega el producto al carrito
    carrito.push({
        id: productoId,
        precio: precio
    });

    // Actualiza la visualización del carrito
    actualizarCarrito();
}

function obtenerPrecio(productoId) {
    // Define una función para obtener el precio basado en el ID del producto
    switch (productoId) {
        case '1':
            return 12000;
        case '2':
            return 42000;
        case '3':
            return 60000;
        default:
            return 0;
    }
}

function actualizarCarrito() {
    // Muestra los productos agregados al carrito en algún lugar de tu página
    let carritoElement = document.getElementById('carrito');
    carritoElement.innerHTML = '';

    carrito.forEach(item => {
        let itemHTML = `<div>Producto ID: ${item.id} - Precio: $${item.precio}</div>`;
        carritoElement.innerHTML += itemHTML;
    });
}
