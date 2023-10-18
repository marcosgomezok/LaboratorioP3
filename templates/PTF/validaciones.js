function add() {
    var new_chq_no = parseInt($('#total_chq').val())+1;
    var new_input="<div><input type='number' id='mu_"+new_chq_no+"' required></div>";
    $('#new_chq').append(new_input);
    $('#total_chq').val(new_chq_no)
  }
  function remove() {
    var last_chq_no = $('#total_chq').val();
    if(last_chq_no>1){
      $('#mu_'+last_chq_no).remove();
      $('#total_chq').val(last_chq_no-1);
    }
  }

  function validarfechas() {
    var fechaD = document.getElementById('fecha_desde').value

    if(fechaD!=""){
        if((new Date(fechaD).getTime()) > (new Date())){    
            alert("Fecha inicio no debe ser posterior a la fecha actual");
            document.getElementById("fecha_desde").value  = "";
        }    
    }
}