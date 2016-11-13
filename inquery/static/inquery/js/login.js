/*
    Use this page to initialize all javascript components used throughout the application
 */

$(document).ready(function() {
    // Initially hide error message
    $('#error_message').hide();

    $('#username').on("click", function() {
        $('#error_message').hide();
    });

    $('#password').on("click", function() {
        $('#error_message').hide();
    });
});

function verify_login() {
    flag = false;

    $('#error_message').hide();

    $.ajax({
        type: "POST",
        async: false,
        url: "/verify_login/",
        data: {email : $('#username').val(), password: $('#password').val()},

        success: function(json) {
            console.log(json['valid']);

            // Show error message if email already exists
            if(json['valid'] == "false") {
                $('#error_message').show();
            }
            else {
                flag = true;
            }
        }
    });

    return flag;
}