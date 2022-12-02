var current_event_id = ""

$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#edit-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const eventID = button.data('source') // Extract info from data-* attributes
        console.log(current_event_id)
        globalThis.current_event_id = eventID
        console.log(current_event_id)
        content = button.data('content') // Extract info from data-* attributes
        
        content = content.replace(/'/g, '"')
        // content = content.replace(/datetime\.date\(\d\d\d\d, \d\d, \d\d\)/g, "YOUR MOTHER")
        
        console.log(content);
        console.log(eventID)
        console.log(content.event_title)

        const content_json = JSON.parse(content)  

        const modal = $(this)
        for (const c in content_json) {
            console.log(c)
        }

        title = content_json.event_title//modal.find("#event-title").data('source')
        modal.find("#event-title").val(title)

        description = content_json.event_description//modal.find("#event-description").data('source')
        modal.find("#event-description").val(description)

        start = content_json.start_date//modal.find("#event-start-date").data('source')
        modal.find("#event-start-date").val(start)

        end = content_json.end_date//modal.find("#event-end-date").data('source')
        modal.find("#event-end-date").val(end)
    })

    $('#submit-edit-event').click(function () {
        console.log($('#edit-modal').find('#event-title').val())
        console.log(globalThis.current_event_id)
        //console.log($('#edit-modal').data('source'))
        request = {
            type: 'POST',
            url: '/edit_event',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'id': globalThis.current_event_id,
                'title': $('#edit-modal').find('#event-title').val(),
                'description': $('#edit-modal').find('#event-description').val(),
                'start_date': $('#edit-modal').find('#event-start-date').val(),
                'end_date': $('#edit-modal').find('#event-end-date').val(),
            }), 
            success: function (res) {
                console.log("Success");
                location.reload();
            },
            error: function () {
                console.log('Error');
            }
        }
        $.ajax(request);
    })

    $('#submit-task').click(function () {
        request = {
            type: 'POST',
            url: '/create_event',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'title': $('#add-modal').find('#event-title').val(),
                'description': $('#add-modal').find('#event-description').val(),
                'start_date': $('#add-modal').find('#event-start-date').val(),
                'end_date': $('#add-modal').find('#event-end-date').val(),
                'park_name': $('#add-modal').find('#igs-01').val()

            }), 
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

    $('.remove').click(function () {
        console.log("ur mom");
        const thing = $(this)
        console.log(thing.data('source'))
        request = {
            type: 'POST',
            url: '/delete_event',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({id: thing.data('source')}),
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

    $('#fetch-new-events').click(function () {
        // console.log("e-mom, discord kitten");
        request = {
            type: 'POST',
            url: '/update_events', 
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