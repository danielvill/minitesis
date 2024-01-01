$(document).ready(function () {
    // Cuando el valor de '.total' o '.abono' cambie, realiza la resta
    $('.total, .abono').on('change', function () {
        // Encuentra el contenedor '.card-body' que contiene este '.total' o '.abono'
        let $cardBody = $(this).closest('.card-body');

        // Obtén los valores de '.total' y '.abono' dentro de este '.card-body'
        let total = parseFloat($cardBody.find('.total').val());
        let abono = parseFloat($cardBody.find('.abono').val());

        // Realiza la resta
        let resultado = total - abono;

        // Muestra el resultado en '.resultado' dentro de este '.card-body'
        $cardBody.find('.resultado').val(resultado);
    });
});

// Obtenemos todos los elementos de fecha
let inputFechas = document.querySelectorAll(".fecha");

// Inicializamos un contador
let contador = 0;

// Iteramos sobre cada elemento de fecha
inputFechas.forEach(function (inputFecha) {
    let fechaInput = new Date(inputFecha.value);
    let fechaActual = new Date();

    // Calculamos la diferencia en milisegundos
    let diferencia = fechaActual - fechaInput;

    // Convertimos la diferencia a días
    let dias = Math.floor(diferencia / (1000 * 60 * 60 * 24));

    // Creamos un elemento p para mostrar el mensaje
    let p = document.createElement("p");

    // Asignamos un ID al elemento p
    p.id = "mensaje" + contador;

    // Verificamos si hay atraso
    if (dias > 0) {
        p.innerText = "Tiene " + dias + " días de atraso";
    } else {
        p.innerText = "No hay atraso";
    }

    // Añadimos el elemento p después del elemento de fecha
    inputFecha.parentNode.appendChild(p);

    // Incrementamos el contador
    contador++;
});
