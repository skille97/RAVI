$(document).ready(function(){
    $(document).on("click", ".data", function(){
      if(document.getElementsByTagName("input").length > 0){
          $("#" + document.getElementsByTagName("input")[0].id).replaceWith("<td class='data' id='" + document.getElementsByTagName("input")[0].id +"'>kek</td>")
      }
      $(this).replaceWith("<input class='data' id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
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
