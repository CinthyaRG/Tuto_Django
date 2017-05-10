$(document).ready(function(){
    $("button").click(function(){
        $.ajax(
            {
                url: "/Home2/",
                success: function(data){
                    $("#div_result").html(data);
                },
                error: function(data){
                    alert(data);
                    $("#div_result").html("ERROR");
                }
            });
        });
    });
