$(document).ready(function(){
    $("button").click(function(){
        $.ajax(
            {
                url: "static/js/hola.txt",
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




