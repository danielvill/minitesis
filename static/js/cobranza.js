function filtrar() {
    // Obtén el valor del filtro
    var filtro = document.getElementById('filtro').value.toUpperCase();
  
    // Obtén los elementos de la lista
    var elementos = document.querySelectorAll(".card-body");
  
    // Itera sobre cada elemento de la lista
    elementos.forEach(function (elemento) {
      var nombre = elemento.querySelector("input[name='nombre']").value;
      if (nombre.toUpperCase().indexOf(filtro) > -1) {
        elemento.style.display = '';
      } else {
        elemento.style.display = 'none';
      }
    });
  }
  