
function agregarAlCarrito(nombre, precio) {
    const producto = { nombre: nombre, precio: precio };
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    carrito.push(producto);
    localStorage.setItem('carrito', JSON.stringify(carrito));
    actualizarCarrito();
}

function actualizarCarrito() {
    const listaCarrito = document.getElementById('listaCarrito');
    const totalCarritoElement = document.getElementById('totalCarrito');
    const cantidadProductosElement = document.getElementById('cantidadProductos');
    listaCarrito.innerHTML = '';
    let carrito = JSON.parse(localStorage.getItem('carrito')) || [];
    let total = 0;
    let cantidadProductos = carrito.length;
    carrito.forEach(producto => {
        const li = document.createElement('li');
        li.textContent = `${producto.nombre}: $${producto.precio}`;
        listaCarrito.appendChild(li);
        total += producto.precio; 
    });
    totalCarritoElement.textContent = `Total: $${total}`;
    cantidadProductosElement.textContent = `Cantidad de productos: ${cantidadProductos}`;
    document.getElementById('carrito').style.display = 'block';
}

function vaciarCarrito() {
    localStorage.removeItem('carrito');
    actualizarCarrito();
}

document.getElementById('verCarrito').addEventListener('click', function(event) {
    event.preventDefault();
    actualizarCarrito();
});

