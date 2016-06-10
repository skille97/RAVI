$(document).ready(function(){
    $(".data").click(function(){
      $(this).replaceWith("<input class='input' type='text'></input>");

    });

    $(window).keydown(function(key){
      if(key.key === "Enter"){
        if(document.getElementsByTagName("input").length > 0){
          console.log(document.getElementsByTagName("input"));

        }
      }
    });

});


window.setInterval(function(){
    $("#table").load(document.URL + ' #table');
    console.log("Reloading table");
}, 5000);
