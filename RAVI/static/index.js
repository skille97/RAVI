var tableEdit = false;
var oldVal = "";

//Variable to store the id of the right clicked cell, that is needed in the rightclick menu(See rightClick.js)
var rightClickedCell = "";


//Get the security token from django and set it in ajax
// Source https://docs.djangoproject.com/en/1.7/ref/contrib/csrf/ and https://stackoverflow.com/questions/22063612/adding-csrftoken-to-ajax-request
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});




//Functions to be defined outside of document.ready
function ajaxRequest (aUrl, aData) {
  $.ajax({
    type: 'POST',
    // Provide correct Content-Type, so that Flask will know how to process it.
    contentType: 'application/json',
    // Encode your data as JSON.
    
    data: JSON.stringify(aData)  ,
    // This is the type of data you're expecting back from the server.
    dataType: 'json',
    url: '/' + aUrl + '/',
    success: function (e) {
      updateStuff();
    }
  });
}

function updateStuff(){
    if (!tableEdit) $("#table").load(document.URL + ' #table', function(){
    fixWhiteColumn();
  }); //location.reload();
}

function hideRow(row) {
    var visible = 1-$("#hide" + row + ":checked").length;
    console.log($("#hide" + row + ":checked").length);
  ajaxRequest("hideRow", {"id": row, "visible" : visible});
    updateStuff();
    }

function columnId(cell){
  var colVal = false;
  var colId = "";
  for (var i = 0; i < cell.length; i++) {
    if (cell[i] === "_") {
      if (!colVal) {
        colVal = true;
      } else {
        colVal = false;
      }
    }
    if (colVal) {
      if (cell[i] !== "_") {
        colId = colId + String(cell[i]);
      }
    }
  }
  return colId;
}

    setInterval(function(){
        updateStuff();
    }, 5000);

function fixWhiteColumn(){
  $(".data").each(function(){
    if(columnId($(this).attr("id")) == 0){
      $(this).css("background-color","#ffffff")
    }
  });
}

//Function will run when all the HTML has been loaded.
$(document).ready(function(){
    function closeInput () {
        if($('input.inputField').length > 0){
            var inputElement = $("input.inputField")[0];
            var id = parseInt($("#" + inputElement.id).parent().attr("id"));

            ajaxRequest("updateRow",{"id": id, "column":columnId(inputElement.id), "newValue": inputElement.value})
            $("#" + inputElement.id).replaceWith("<td class='data' id='" + inputElement.id +"' style='background-color: " + oldColour + "'>" + inputElement.value + "</td>");
            tableEdit = false;
        }
    }

    $(document).on("click", ".data", function(event){
        if (!$(this).attr('id').startsWith("Cell_0")) {
            event.stopPropagation();
            closeInput();
            oldVal = $(this).html();
      oldColour = $(this).css("background-color");
      console.log($(this).css("background-color"));
            $(this).replaceWith("<input class='inputField' class='data' id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
            tableEdit = true;
        }
    });

  $(document).on("contextmenu", ".data", function(event){
    rightClickedCell = $(this).attr("id");

  });
  $(document).on("contextmenu", "body", function(event){
    if(event.target.className !== "data"){
      rightClickedCell = "";
    }
  });

    $(window).keydown(function(key){
        if(key.key === "Enter" || key.keyCode === 13){
            closeInput();
            tableEdit = false;
        }
        if(key.keyCode === 27){
            if(document.getElementsByTagName("input").length > 0){
                var inputElement = document.getElementsByTagName("input")[0];
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
            closeInput();
            //Function runs when add cell button is pressed
            var name = prompt("name", "test");
            if(name){
                ajaxRequest("addRow", {"text": name});
            }
            updateStuff();
    });
  fixWhiteColumn();
});
