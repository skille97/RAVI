$(document).ready(function(){
    $(".data").click(function(){
      $(this).replaceWith("<input type='text'></input>");

    });

    $(window).keydown(function(key){
      if(key.key === "Enter"){
        if(document.getElementsByTagName("input").length > 0){
          console.log(document.getElementsByTagName("input"));
        }
      }
    });
});
