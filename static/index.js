var tableEdit = false;
var oldVal = "";
var genBoxOld = "";
var genBoxEdit = false;

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

  $(document).on("click", ".data", function(event){
    event.stopPropagation();
    closeInput();
    oldVal = $(this).html();
    $(this).replaceWith("<input class='inputField' id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
    tableEdit = true;
  });

  $(document).on("click", ".genBox", function(event){
    event.stopPropagation();
    genBoxOld = $(this).html();
    $(this).replaceWith("<textarea class='genBoxEdit'>" + $(this).html() + "</textarea>");
    genBoxEdit = true;
  });

  function updateGenBox(safe){
    if(safe && genBoxEdit){
      ajaxRequest("setGenBox", {"val": $(".genBoxEdit").val()});
      $(".genBoxEdit").replaceWith("<div class='genBox'>" + $(".genBoxEdit").val() + "</div>");
    }else{
      $(".genBoxEdit").replaceWith("<div class='genBox'>" + genBoxOld + "</div>");
    }
    genBoxEdit = false;
  };

  $(window).keydown(function(key){
    if(key.key === "Enter" || key.keyCode === 13){
      closeInput();

      updateGenBox(true);

      tableEdit = false;
    }
    if(key.keyCode === 27){
      updateGenBox(false);
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
          $("#" + inputElement.id).replaceWith("<td class='data' id='" + inputElement.id +"'>" + oldVal + "</td>");
      }
      tableEdit = false;
    }
  });

  $(window).click(function(){
    //Input needs to go out of focus when anywhere else than the element itself is clicked
    closeInput();
  });

  $(document).on("click", ".inputField",function(event){
    event.stopPropagation();
  })

  $("#add").click(function(){
    //Function runs when add cell button is pressed
    var name = prompt("name", "test");
    if(name){
    ajaxRequest("addRow", {"text": name});
    }
    updateStuff();
  });
});

function updateStuff(){
  if(!tableEdit){ $("#table").load(document.URL + ' #table'); }
  if(!genBoxEdit){ $("#genBox").load(document.URL + ' #genBox'); }
}


setInterval(function(){
	updateStuff();
}, 5000);
