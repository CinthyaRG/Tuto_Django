$(document).ready(function(){
    $("#test-ajax").click(function(){
        $.ajax(
            {
                url: "resultado",
                success: function(result){
                    $("#div_result").html(result);
                    console.log("Sucess");
                },
                error: function(result){
                    $("#div_result").html("ERROR");
                    console.log("Error");
                }
            });
        });
    });