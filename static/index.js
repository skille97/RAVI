$(document).ready(function(){
  function closeInput () {
    if(document.getElementsByTagName("input").length > 0){
        var inputElement = document.getElementsByTagName("input")[0];
        $("#" + inputElement.id).replaceWith("<td class='data' id='" + inputElement.id +"'>" + inputElement.value + "</td>")
    }
  }

  $(document).on("click", ".data", function(){
    closeInput();
    $(this).replaceWith("<input id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
  });

  $(window).keydown(function(key){
    if(key.key === "Enter"){
      closeInput();
    }
  });

  $(window).click(function(){
    console.log("Dank");
  });

  $("#add").click(function(){
    //Function runs when add cell button is pressed
    console.log("Dank2");
    var name = prompt("name", "test");
    $.ajax({
      type: 'POST',
      // Provide correct Content-Type, so that Flask will know how to process it.
      contentType: 'application/json',
      // Encode your data as JSON.
      data: JSON.stringify({"text":name}),
      // This is the type of data you're expecting back from the server.
      dataType: 'json',
      url: '/addRow/',
      success: function (e) {
          console.log(e);
      }
    });
  });
});
