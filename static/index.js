$(document).ready(function(){
    $(document).on("click", ".data", function(){
      if(document.getElementsByTagName("input").length > 0){
          console.log(document.getElementsByTagName("input")[0].id.value);
          $("#" + document.getElementsByTagName("input")[0].id).replaceWith("<td class='data' id='" + document.getElementsByTagName("input")[0].id +"'>" + document.getElementsByTagName("input")[0].id.value + "</td>")
      }
      $(this).replaceWith("<input id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
      console.log("test");
    });

    $(window).keydown(function(key){
      if(key.key === "Enter"){
        if(document.getElementsByTagName("input").length > 0){
          console.log(document.getElementsByTagName("input"));

        }
      }
    });
});
