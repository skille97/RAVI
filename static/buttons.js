function newYrow(){
  console.log("test");
  $.ajax({
    type: 'POST',
    // Provide correct Content-Type, so that Flask will know how to process it.
    contentType: 'application/json',
    // Encode your data as JSON.
    data: JSON.stringify({"cell":"1,3", "data": "hej"}),
    // This is the type of data you're expecting back from the server.
    dataType: 'json',
    url: '/changeCell/',
    success: function (e) {
        console.log(e);
    }
  });
}
