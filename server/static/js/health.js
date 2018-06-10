$(document).ready(function(){
  //set time in milliseconds
  var timer = 1000;

  //set interval method to make requests in an interval
  setInterval(function(){
    //in AJAX if method type is not defined than by default it is a GET method.
    $.ajax({
      url:"/health",
      success:function(result){
        //console.log(result);
        //Parse the results and construct a chart out of them in chart.js
        //console.log(JSON.parse(result));

        var jsonResult = JSON.parse(result);

        var items = jsonResult.data;
        /*
        //get data elements
        var Series_reference = [];
        var Period = [];
        var Type = [];
        var Data_value = [];
        var Lower_CI = [];

        //iterate through the array of results and then append data to corresponding fields.
        */

        for(var i-0;i<items.length;i++){

        }
      },
      error:function(error){
        console.log(error);
      }
    });
  },timer);
});
