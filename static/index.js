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
		console.log("test");
	});

	$(window).keydown(function(key){
		if(key.key === "Enter"){
			closeInput();
		}
	});
});


window.setInterval(function(){
	$("#table").load(document.URL + ' #table');
	console.log("Reloading table");
}, 5000);
