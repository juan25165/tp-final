// document.addEventListener("DOMContentLoaded", function() {
//     window.addEventListener("load", function() {
//         const loader = document.querySelector('.loader');
//         const content = document.querySelector('.content');

//         setTimeout(() => {
//             loader.style.opacity = 0;
//             loader.style.visibility = 'hidden';
//             content.style.display = 'block';
//         }, 2000); // Demora de 500ms para transición
//     });
// });

function validarFormulario(event) {
    // Obtener referencias a los campos del formulario
    const nombre = document.getElementById('nombre');
    const apellido = document.getElementById('apellido');
    const email = document.getElementById('email');
    const asunto = document.getElementById('asunto');
    const mensaje = document.getElementById('mensaje');

    const mensajeError = document.getElementById('mensajeError');

    // Verificar si los campos están vacíos
    if (!nombre.value.trim() || !apellido.value.trim() || !email.value.trim() || !telefono.value.trim()) {
        // Evitar que el formulario se envíe
        event.preventDefault();
        // Mostrar mensaje de error
        mensajeError.textContent = 'Por favor, completa todos los campos obligatorios.';
        mensajeError.style.display = 'block'
    } else {
        window.location.href = "registro-exitoso.html";
    }
}

// Asociar la función validarFormulario al evento submit del formulario
document.getElementById('miFormulario').addEventListener('submit', validarFormulario);
