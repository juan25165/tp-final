function validarFormulario(event) {
    // Obtener referencias a los campos del formulario
    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const email = document.getElementById('email');
    const telefono = document.getElementById('telefono');  // Corrected missing telefono

    const mensajeError = document.getElementById('mensajeError');

    // Verificar si los campos están vacíos
    if (!nombre.value.trim() || !apellido.value.trim() || !email.value.trim() || !telefono.value.trim()) {
        // Evitar que el formulario se envíe
        event.preventDefault();
        // Mostrar mensaje de error
        mensajeError.textContent = 'Por favor, completa todos los campos obligatorios.';
        mensajeError.style.display = 'block';
    } else {
        window.location.href = "registroexitoso.html";
    }
}

// Asociar la función validarFormulario al evento submit del formulario
document.getElementById('miFormulario').addEventListener('submit', validarFormulario);