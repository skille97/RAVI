$(document).ready(function(){
    $(".data").click(function(){
      if(document.getElementsByTagName("input").length > 0){
          $("#" + document.getElementsByTagName("input")[0].id).replaceWith("<td>test</td>")
          console.log(document.getElementsByTagName("input")[0])
      }
      $(this).replaceWith("<input id='" + $(this).attr("id") + "' type='text' value='" + $(this).html() + "'></input>");
    });

    $(window).keydown(function(key){
      if(key.key === "Enter"){
        if(document.getElementsByTagName("input").length > 0){
          console.log(document.getElementsByTagName("input"));

        }
      }
    });
});
