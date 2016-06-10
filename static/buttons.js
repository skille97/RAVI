function newRow(axis){
  console.log("test");
  var name = prompt("Hvad skal den nye række hedde?");
  if(name != null  && name != "null" && name != "" && name != "undefined" && name != " "){
    if(axis == "y" || axis == "x"){
      $.ajax({
        type: 'POST',
        // Provide correct Content-Type, so that Flask will know how to process it.
        contentType: 'application/json',
        // Encode your data as JSON.
        data: JSON.stringify({"axis":axis, "name": name}),
        // This is the type of data you're expecting back from the server.
        dataType: 'json',
        url: '/addRow/',
        success: function (e) {
            console.log(e);
            alert("Request sendt");
        }
      });
    }
  }
}

function moveRow(axis, direc){
  var row = parseInt(prompt("Hvilken række skal flyttes?"));
  if(!isNaN(row) && row != "none"){
    $.ajax({
      type: 'POST',
      // Provide correct Content-Type, so that Flask will know how to process it.
      contentType: 'application/json',
      // Encode your data as JSON.
      data: JSON.stringify({"axis":axis, "row": row, "direc" : direc}),
      // This is the type of data you're expecting back from the server.
      dataType: 'json',
      url: '/moveRow/',
      success: function (e) {
          console.log(e);
          alert("Request sendt");
      }
    });
  }
}


function changeCell(){
  var cell = prompt("Hvilken celle skal ændres? Adskild med komma. Fx '2,3'");
  if(cell.indexOf(",") > -1){
    var input = prompt("Hvad skal den ændres til?");
    $.ajax({
      type: 'POST',
      // Provide correct Content-Type, so that Flask will know how to process it.
      contentType: 'application/json',
      // Encode your data as JSON.
      data: JSON.stringify({"cell":cell, "data": input}),
      // This is the type of data you're expecting back from the server.
      dataType: 'json',
      url: '/changeCell/',
      success: function (e) {
          console.log(e);
          alert("Request sendt");
      }
    });

  }

}
