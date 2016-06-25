// JAVASCRIPT (jQuery)

$(".custom-menu").hide();

function cellColor(newColor){
  $("#" + rightClickedCell).css("background-color", newColor);
  /*var colVal = false;
  var colId = "";
  for (var i = 0; i < rightClickedCell.length; i++) {
    if (rightClickedCell[i] === "_") {
      if (!colVal) {
        colVal = true;
      } else {
        colVal = false;
      }
    }
    if (colVal) {
      if (rightClickedCell[i] !== "_") {
        colId = colId + String(rightClickedCell[i]);
      }
    }
  }*/
  ajaxRequest("updateColour", "test");
  //ajaxRequest("/updateColour/", {colour : newColor, row : "kek", column : colId});
}

// Trigger action when the contexmenu is about to be shown
$(document).bind("contextmenu", function (event) {

    // Avoid the real one
    event.preventDefault();

    // Show contextmenu
    $(".custom-menu").finish().toggle().


    // In the right position (the mouse)
    css({
        'margin-top': event.pageY - 130 + "px",
        'margin-left': event.pageX + "px"
    });
});


// If the document is clicked somewhere
$(document).bind("mousedown", function (e) {

    // If the clicked element is not the menu
    if (!$(e.target).parents(".custom-menu").length > 0) {

        // Hide it
        $(".custom-menu").hide(100);
    }
});


// If the menu element is clicked
$(".custom-menu li").click(function(){
    // This is the triggered action name
    switch($(this).attr("data-action")) {

        // A case for each action. Your actions here
        case "red": cellColor("#ff0000"); break;
        case "yellow": cellColor("#ffe600"); break;
        case "green": cellColor("#63eb05"); break;
    }

    // Hide it AFTER the action was triggered
    $(".custom-menu").hide(100);
  });
