var current_event_id = ""

$(document).ready(function () {
    
    $('#diggity_dawg').click(function () {
        console.log("HOT!");
        request = {
            type: 'POST',
            url: '/diggity_dawg', 
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