var tableEdit = false;
var oldVal = "";

//Variable to store the id of the right clicked cell, that is needed in the rightclick menu(See rightClick.js)
var rightClickedCell = "";

//Functions to be defined outside of document.ready
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
  ajaxRequest("hideRow", {"id": row});
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
			$("#" + inputElement.id).replaceWith("<td class='data' id='" + inputElement.id +"'>" + inputElement.value + "</td>");
			tableEdit = false;
		}
	}

	$(document).on("click", ".data", function(event){
		if (!$(this).attr('id').startsWith("Cell_0")) {
			event.stopPropagation();
			closeInput();
			oldVal = $(this).html();
			$(this).replaceWith("<input class='inputField' class='data' id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
			tableEdit = true;
		}
	});

	/*$(document).on("contextmenu", ".data", function(event){
    rightClickedCell = $(this).attr("id");
    console.log(rightClickedCell);
	});*/

  $(document).on("contextmenu", ".data", function(event){
    rightClickedCell = $(this).attr("id");

    /*rightClickedCell = "dank click";
    if($(this).attr("class") === "data"){
      console.log("cell");
      rightClickedCell = $(this).attr("id");
    }
    console.log(rightClickedCell);*/
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
