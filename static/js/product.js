$(document).ready(function () {
    let maxField = 20; // Número máximo de campos a agregar
    let addButton = $('#addButton'); // Selector del botón de agregar
    let wrapper = $('.productos'); // Contenedor de campo de entrada
    let fieldHTML = '<div class="productos"><input type="text" name="codigo[]" class="codigo" placeholder="codigo"><input type="text" name="precio[]" class="precio" placeholder="precio"><input type="text" name="cantidad[]" class="cantidad" placeholder="cantidad"><input type="text" name="resultado[]" class="resultado" placeholder="resultado"><a href="javascript:void(0);" class="remove_button">Eliminar</a></div>'; // HTML del campo de entrada con un enlace para eliminar el campo
    let x = 1; // Contador de campo inicial

    // Una vez que se hace clic en el botón de agregar
    $(addButton).click(function () {
        // Verificar el número máximo de campos de entrada
        if (x < maxField) {
            x++; // Incrementar el contador de campo
            $(wrapper).append(fieldHTML); // Agregar campo html
        }
    });

    // Una vez que se hace clic en el enlace de eliminar
    $(wrapper).on('click', '.remove_button', function (e) {
        e.preventDefault();
        $(this).parent('div').remove(); // Eliminar el div del campo de entrada
        x--; // Decrementar el contador de campo
    });

    // Agrega esta función para calcular el resultado y la suma total
    function calcularTotal() {
        let total = 0;
        //solo para que el apartado de productos sume los valores debo colocar el #productos   
        $('.productos').each(function () {
            let cantidad = parseFloat($(this).find('.cantidad').val()) || 0;
            let precio = parseFloat($(this).find('.precio').val()) || 0;

            // Calcula el resultado y actualiza el campo "Resultado"
            let resultado = cantidad * precio;
            $(this).find('.resultado').val(resultado);

            // Suma al total
            total += resultado;
        });

        // Actualiza el campo "Total"
        $('#total').val(total);
    }
     // Llama a la función cuando se cargue la página y cuando se realicen cambios
     calcularTotal();
    $(wrapper).on('change', 'input', calcularTotal);
});