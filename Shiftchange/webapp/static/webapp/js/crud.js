function cargar(url) {
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
      document.getElementById("demo").innerHTML = this.responseText;
     }
   };
   xhttp.open("GET", url, true);
   xhttp.send();
}


function cambioEstado(url) {
  var xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
     if (this.readyState == 4 && this.status == 200) {
           cargar('webapp/aplicacion_empleado/');
     }
   };
   xhttp.open("GET", url, true);
   xhttp.send();
}


function agregarEmpleado() {
  $.post("webapp/aplicacion_empleado/",
          {
            nombre: $('[name=nombre]').val(),
            apellido: $('[name=apellido]').val(),
            documento: $('[name=documento]').val(),
            correo: $('[name=correo]').val(),
            activo: $('[name=estado]').val()
          },
          function(data,status){
              console.log("Data: " + data + "\nStatus: " + status);
              cargar('/aplicacion_empleado/');
          });
}
