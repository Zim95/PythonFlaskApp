$(document).ready(function(){
    //for toggling divs
    function switching(val){
      //hide all content
      $('.content').css("display","none");
      //show a particular content as per value provided.
      $("#"+val).css("display","block");
    }

    //Switching between divs. New switches can be added below.
    $("#mainButton").click(function(){
      switching("page-main");
    });

    $(".heading").click(function(){
      switching("page-main");
    });

    $("#healthButton").click(function(){
      switching("dashboard-health");
    });
});
