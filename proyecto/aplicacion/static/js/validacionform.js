function validarFormulario() {
    var nombre = document.getElementById("nombre").value;
    var apellido = document.getElementById("apellido").value;
    var numero = document.getElementById("numero").value;
    var edad = document.getElementById("edad").value;

    if (nombre.length < 3 || nombre.length > 15) {
        alert("El nombre debe tener entre 3 y 15 caracteres.");
        return false;
    }

    if (apellido.length < 3 || apellido.length > 15) {
        alert("El apellido debe tener entre 3 y 15 caracteres.");
        return false;
    }

    if (edad < 15){
        alert("Debes tener 15 o mas años");
        return false;
    }

    if (!numero.startsWith("+569")) {
        alert("El número de teléfono debe comenzar con +569.");
        return false;
    }

    if (numero.length !== 12) {
        alert('El número de teléfono debe tener 12 caracteres, incluyendo +569.');
        return false;
    }

    alert(" Hemos recibido sus datos, en la brevedad nos pondremos en contacto. ")
    return true;
}

