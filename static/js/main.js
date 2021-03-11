$(document).ready(function() {

    $("#phone_number_form").on('submit', function(){
        var phone_number = $("#phone_number_form #id_phone_number").val()
        if ( phone_number == '' ){
            $("#phone_number_form #id_phone_number").removeClass('is-valid')
            $("#phone_number_form #id_phone_number").removeClass('was-validated')
            return false;
        }
        phone_number = phone_number.replaceAll('-', '' );
        var csrf_token = $("input[name=csrfmiddlewaretoken]").val()
        $.ajax({
            type: "POST",
            url: $("#phone_number_form").data("url"),
            data: {
                'phone_number': phone_number,
                'otp_number': null,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(response){
                if (response.status == false ){
                    switch( response.case) {
                        case "register":
                            if ( response.details == "User doen't exists, Please register") {
                                $("#id_phone_number_warning").show().text( response.details)
                                return false;
                            }
                            window.location.href = response.url
                    }
                }
                else {
                    switch (response.case ){
                        case "validate":
                            $("#phone_number_form").hide()
                            $("#otp_number_form").show()
                    }
                }
            },
        });
        return false;
    });
    //validate otp for reset password
    $("#otp_number_form").on('submit', function(){
        var phone_number = $("#phone_number_form #id_phone_number").val().replaceAll('-', '')
        var otp_number = $("#otp_number_form #id_otp_value").val()
        if ( otp_number == '' ){
            $("#otp_number_form #id_otp_value").removeClass('is-valid')
            $("#otp_number_form #id_otp_value").removeClass('was-validated')
            return;
        }
        otp_number = otp_number.replaceAll('-', '' );
        var csrf_token = $("input[name=csrfmiddlewaretoken]").val()
        $.ajax({
            type: "POST",
            url: $("#otp_number_form").data("url"),
            data: {
                'phone_number': phone_number,
                'otp_number': otp_number,
                csrfmiddlewaretoken: csrf_token
            },
            success: function(response){
                if (response.status == false ){
                    switch( response.case) {
                        case "register":
                            alert(response.url)
                            window.location.href = response.url
                        case "validate":
                            if (response.details == "Incorrect OTP" ) {
                                $("#id_otp_warning").show().text(response.details)
                            }
                    }
                }
                else {
                    switch (response.case ){
                        case "validate":
                            $("#phone_number_form").hide()
                            $("#otp_number_form").show()
                            window.location.href = response.url
                    }
                }
            },
        });
        return false;
    })
})