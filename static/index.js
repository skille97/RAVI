var tableEdit = false;
var oldVal = "";

$(document).ready(function(){
	function closeInput () {
		console.log($('input.inputField'));
		if($('input.inputField').length > 0){
			var inputElement = $("input.inputField")[0];
			var colVal = false;
			var colId = "";
			for (var i = 0; i < inputElement.id.length; i++) {
				if (inputElement.id[i] === "_") {
					if (!colVal) {
						colVal = true;
					} else {
						colVal = false;
					}
				}
				if (colVal) {
					if (inputElement.id[i] !== "_") {
						colId = colId + String(inputElement.id[i]);
					}
				}
			}
			var id = parseInt($("#" + inputElement.id).parent().attr("id"));
			ajaxRequest("updateRow",{"id": id, "column":colId, "newValue": inputElement.value})
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
				updateStuff();
			}
		});
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

	$(window).keydown(function(key){
		if(key.key === "Enter" || key.keyCode === 13){
			closeInput();
			tableEdit = false;
		}
		if(key.keyCode === 27){
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
		if(!tableEdit){
			//Function runs when add cell button is pressed
			var name = prompt("name", "test");
			if(name){
				ajaxRequest("addRow", {"text": name});
			}
			updateStuff();}
	});
});

function updateStuff(){
	if (!tableEdit) $("#table").load(document.URL + ' #table'); //location.reload();
}

function hideRow(row) {
	$.ajax({
		type: 'POST',
		// Provide correct Content-Type, so that Flask will know how to process it.
		contentType: 'application/json',
		// Encode your data as JSON.
		data: JSON.stringify({'id': row}),
		// This is the type of data you're expecting back from the server.
		dataType: 'json',
		url: '/hideRow/',
		success: function (e) {
			console.log(e);
			updateStuff();
		}
	});}


	setInterval(function(){
		updateStuff();
	}, 5000);
