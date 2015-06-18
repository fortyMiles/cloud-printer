/*
 * To let the button could not be pressed init.
 */
$(document).ready(function(){
  alert('gogogo');
  $("#submitID").hide();
});


function couldSubmit(){
  $(":submit").attr('disabled',false)
}

