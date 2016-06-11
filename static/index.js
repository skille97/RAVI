var tableEdit = false;

$(document).ready(function(){
  function closeInput () {
    if(document.getElementsByTagName("input").length > 0){
        var inputElement = document.getElementsByTagName("input")[0];
        var colVal = false;
        var colId = "";
        for (var i = 0; i < inputElement.id.length; i++) {
          if (inputElement.id[i] === "_") {
            if (!colVal) {
                colVal = true;
            }else{
                colVal = false;
            }
          }
          if(colVal){
            if (inputElement.id[i] !== "_") {
              colId = colId + String(inputElement.id[i]);
            }
          }
        }
        ajaxRequest("updateRow",{"id":parseInt($("#" + inputElement.id).parent().attr("id")) + 1, "value":colId, "newValue": inputElement.value})
        $("#" + inputElement.id).replaceWith("<td class='data' id='" + inputElement.id +"'>" + inputElement.value + "</td>");
    }
  }

  function ajaxRequest (aUrl, aData) {
    $.ajax({
      type: 'POST',
      // Provide correct Content-Type, so that Flask will know how to process it.
      contentType: 'application/json',
      // Encode your data as JSON.
      data: JSON.stringify(aData),
      // This is the type of data you're expecting back from the server.
      dataType: 'json',
      url: '/' + aUrl + '/',
      success: function (e) {
          console.log(e);
      }
    });
  }

  $(document).on("click", ".data", function(){
    closeInput();
    $(this).replaceWith("<input id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
    tableEdit = true;
  });

  $(window).keydown(function(key){
    if(key.key === "Enter"){
      closeInput();
      tableEdit = false;
    }
  });

  $(window).click(function(){
  });

  $("#add").click(function(){
    //Function runs when add cell button is pressed
    var name = prompt("name", "test");
    ajaxRequest("addRow", {"text": name});
  });
});

function updateStuff(){
  if(!tableEdit){ $("#table").load(document.URL + ' #table'); }
}


setInterval(function(){
	updateStuff();
}, 5000);
