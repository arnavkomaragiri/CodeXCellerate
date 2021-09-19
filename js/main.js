(function ($) {
    "use strict";

    $(function(){
        $("#lang").on('click', '#11', function(){
          $("#dropdownMenuButton").text($(this).text());
          $("#dropdownMenuButton").val($(this).text());
        });
        $("#task").on('click', '#21', function(){
            $("#dropdownMenuButton1").text($(this).text());
            $("#dropdownMenuButton1").val($(this).text());
        });
    });

    function analyzeCode() {
        var code = $("#code").val();    
        const options = {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(data)
        };
        return await fetch("http://localhost:8000/", options)
            .then(response => response.json())
            .then(data => {
                console.log(data);
                return data;
            })
            .catch(error => {
                console.error('Request Failed:', error)
            });
    }

    
    $(".contact-form-btn").on('submit', function() {
        alert("I am here")
        var code = document.getElementById("code").innerHTML;
        analyzeCode(code).then(data => {
            document.getElementById("code").innerHTML = data;
        })
    });

    // var input = $('.validate-input .input100');
    // $('.validate-form').on('submit',function(){
    //     var check = true;

    //     for (var i=0; i<input.length; i++) {
    //         if (validate(input[i]) == false){
    //             showValidate(input[i]);
    //             check=false;
    //         }
    //     }

    //     return check;
    // });

    $('.validate-form .input100').each(function(){
        $(this).focus(function(){
           hideValidate(this);
        });
    });

    function showValidate(input) {
        var thisAlert = $(input).parent();

        $(thisAlert).addClass('alert-validate');
    }

    function hideValidate(input) {
        var thisAlert = $(input).parent();
        $(thisAlert).removeClass('alert-validate');
    }
})(jQuery);