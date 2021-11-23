// username checker
$(document).ready(function () {
    $("#username").keyup(function () {
        var username = $(this).val();
        if (username != "") {
            $.ajax({
                url: '/username/',
                type: 'POST',
                data: { username: username }
            }).done(function (response) {
                // console.log(response);
                if (response == "False") {
                    if ($("#username-checker").hasClass('fa-check-circle')){
                        $('#username-checker').removeClass('fa-check-circle')
                    }
                    $('#username-checker').addClass('fa-times-circle')

                    
                }
                else if(response == "True") {
                    if ($("#username-checker").hasClass('fa-times-circle')) {
                        $('#username-checker').removeClass('fa-times-circle')
                    }
                    $('#username-checker').addClass('fa-check-circle')
                }
                else{
                    if ($("#username-checker").hasClass('fa-check-circle')) {
                        $('#username-checker').removeClass('fa-check-circle')
                    }
                    if ($("#username-checker").hasClass('fa-times-circle')) {
                        $('#username-checker').removeClass('fa-times-circle')
                    }

                }
            })
                .fail(function () {
                    console.log("failed");
                })
        }
        else {
            $(".username-status").remove();
            console.log("done")
        }
    });
})