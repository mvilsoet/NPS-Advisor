var current_event_id = ""

$(document).ready(function () {
    
    $('#diggity_dawg').click(function () {
        console.log("HOT!");
        request = {
            type: 'GET',
            url: '/',
            contentType: 'application/json;charset=UTF-8',
            success: function (res) {
                console.log("Success");
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        }

        $.ajax(request);
    });
});