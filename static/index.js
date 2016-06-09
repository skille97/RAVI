$(document).ready(function(){
    $(".data").click(function(){
      var response = prompt("Enter value for cell:","Value")
      $(this).html(response);
    });
});
