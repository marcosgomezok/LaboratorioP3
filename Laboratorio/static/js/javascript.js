function disableBox(value){
    if(value=="observado"){
      document.getElementById("observacion").required = true;
    }else{
      document.getElementById("observacion").required = false
      document.getElementById("observacion").required = false;
    }
}

/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
  var x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}