$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#edit-modal').on('show.bs.modal', function (event) {
        const button = $(event.relatedTarget) // Button that triggered the modal
        const eventID = button.data('source') // Extract info from data-* attributes
        content = button.data('content') // Extract info from data-* attributes
        
        content = content.replace(/'/g, '"')
        
        console.log(content);
        console.log(eventID)
        console.log(content.event_title)
        //console.log($(this).data('source'))
        // console.log(content[1]);
        // console.log(content[19]);
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

        // if (taskID === 'New Event') {
        //     modal.find('.modal-title').text(taskID)
        //     $('#task-form-display').removeAttr('taskID')
        // } else {
        //     modal.find('.modal-title').text('Edit Task ' + taskID)
        //     $('#task-form-display').attr('taskID', taskID)
        // }

        // if (content) {
        //     modal.find('.form-control').val(content);
        // } else {
        //     modal.find('.form-control').val('');
        // }
    })
    // $('#edit-button').click(function () {
    //     console.log("sdgsdfgdfshgdsnldfjkgnsjlkhjsghdjsgfdlkhjsdghjlsgdfhjklsgdhjlkgfdlhjksgfdhjlksgfdlkhjsgfhjkdllhjksdgfcsgfbnbjksgbhljkflhughlsgfdlhjgfhldhkljgfdhljksgfhljkgshkjlsgfhkjlsgdfhjklsgdfhjlksgfdhkjlsgfdhlhskdgfhksgfdhjklsgdhjlsgkdfhjlk");
    // });

    $('#submit-edit-event').click(function () {
        console.log($('#edit-modal').find('#event-title').val())
        //console.log($('#edit-modal').data('source'))
        // request = {
        //     type: 'POST',
        //     url: '/edit_event',
        //     contentType: 'application/json;charset=UTF-8',
        //     data: JSON.stringify({
        //         'id': $(this).data('source'),
        //         'title': $('#add-modal').find('#event-title').val(),
        //         'description': $('#add-modal').find('#event-description').val(),
        //         'start_date': $('#add-modal').find('#event-start-date').val(),
        //         'end_date': $('#add-modal').find('#event-end-date').val(),
        //     }), 
        //     success: function (res) {
        //         console.log("Success");
        //         location.reload();
        //     },
        //     error: function () {
        //         console.log('Error');
        //     }
        // }
        // $.ajax(request);
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
});