$(document).ready(function () {
    // example: https://getbootstrap.com/docs/4.2/components/modal/
    // show modal
    $('#task-modal').on('show.bs.modal', function (event) {
        // const button = $(event.relatedTarget) // Button that triggered the modal
        // const taskID = button.data('source') // Extract info from data-* attributes
        // const content = button.data('content') // Extract info from data-* attributes

        // const modal = $(this)
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


    $('#submit-task').click(function () {
        request = {
            type: 'POST',
            url: '/create_event',
            contentType: 'application/json;charset=UTF-8',
            data: JSON.stringify({
                'title': $('#task-modal').find('#event-title').val(),
                'description': $('#task-modal').find('#event-description').val(),
                'start_date': $('#task-modal').find('#event-start-date').val(),
                'end_date': $('#task-modal').find('#event-end-date').val(),
                'park_name': $('#task-modal').find('#igs-01').val()

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
});