$(document).ready(function() {
    //phone number validation and mask
    $("input[id='id_phone_number']").on("input", function () {
        $("input[id='id_phone_number2']").val(destroyMask(this.value));
        this.value = createMask($("input[id='id_phone_number2']").val());
    })

    function createMask(string) {
        console.log(string)
        return string.replace(/(\d{3})(\d{3})(\d{3})/, "$1-$2-$3");
    }

    function destroyMask(string) {
        console.log(string)
        return string.replace(/\D/g, '').substring(0, 10);
    }

    //otp validation and mask
    $("input[id='id_otp_value']").on("input", function () {
        $("input[id='id_otp_value2']").val(destroyMask(this.value));
        this.value = createMask($("input[id='id_otp_value2']").val());
    })

    function createMask(string) {
        console.log(string)
        return string.replace(/(\d{3})(\d{3})(\d{3})/, "$1-$2-$3");
    }

    function destroyMask(string) {
        console.log(string)
        return string.replace(/\D/g, '').substring(0, 10);
    }
})