$(document).ready(function() {
    var csrf_token = $("input[name=csrfmiddlewaretoken]").val()
    $("#register_phone1").on('click', function() {
        var serializedDate = $("#registerPhoneForm").serialize();
        $.ajax({
            url: $("#registerPhoneForm").attr("action"),
            data: serializedDate,
            type: 'post',
            success: function(response){
                alert(JSON.stringify(response))
                if ( response.status ) {
                    window.location = $("#registerPhoneForm").data("url")
                }
                else {
                    $("#registerPhoneForm").focus()
                    alert("6666")
                    $("#registerPhoneForm")[0].reset();
                    return
                }
            }
        })
    });

})