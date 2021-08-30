function make_upload_area(method, url, mediaSavePath)
{
    $("#upload-area").dmUploader({
        url: url,
        method: method,
        dataType: 'json',
        fieldName: 'uploadFile',
        //allowedTypes: "image/*",
        extFilter: ["jpg", "jpeg", "png", "gif", "xls", "xlsx"],
        queue: true, // Files will upload one by one.
        auto: true, // Files will start uploading right after they are added.
        dnd: true, // Enables Drag and Drop.
        hookDocument: true, //  Disables dropping files on $(document).
        multiple: true, // Allows the user to select or drop multiple files at the same time.
        maxFileSize: 3000000, // 3 Megs
        extraData: {
            'mediaSavePath': mediaSavePath
        },
        headers: {
            'X-CSRFToken': $("input[name=csrfmiddlewaretoken]").val()
        },

        onInit: function () { // Widget it's ready to use.
            console.log('Callback: Plugin initialized');
        },
        onComplete: function () { // All pending files are completed.
            console.log('Callback: Complete');
        },

        onNewFile: function (id, file) {
            // When a new file is added using the file selector or the DnD area
            // ui_add_log('New file added #' + id);
            ui_multi_add_file(id, file);
        },
        onBeforeUpload: function (id) {
            // about tho start uploading a file
            // ui_add_log('Starting the upload of #' + id);
            ui_multi_update_file_progress(id, 0, '', true);
            ui_multi_update_file_status(id, 'uploading', 'Uploading...');
        },
        onUploadProgress: function (id, percent) {
            // Updating file progress
            ui_multi_update_file_progress(id, percent);
        },
        onUploadSuccess: function (id, data) {
            // A file was successfully uploaded
            // ui_add_log('Server Response for file #' + id + ': ' + JSON.stringify(data));
            // ui_add_log('Upload of file #' + id + ' COMPLETED', 'success');
            if (data.Code == '0000') {
                ui_multi_update_file_status(id, 'success', 'Upload Complete');
                ui_multi_update_file_progress(id, 100, 'success', false);
            }
            else {
                ui_multi_update_file_status(id, 'danger', data.Message);
                ui_multi_update_file_progress(id, 0, 'danger', false);
            }
        },
        onUploadError: function (id, xhr, status, message) {
            // Happens when an upload error happens
            ui_multi_update_file_status(id, 'danger', message);
            ui_multi_update_file_progress(id, 0, 'danger', false);
        },
        onFallbackMode: function () {
            // When the browser doesn't support this plugin :(
            ui_add_log('Plugin cant be used here, running Fallback callback', 'danger');
        },
        onFileSizeError: function (file) {
            ui_add_log('File \'' + file.name + '\' cannot be added: size excess limit', 'danger');
        }
    });
}

function ui_add_log(message, color)
{
    var d = new Date();

    var dateString = (('0' + d.getHours())).slice(-2) + ':' +
        (('0' + d.getMinutes())).slice(-2) + ':' +
        (('0' + d.getSeconds())).slice(-2);

    color = (typeof color === 'undefined' ? 'muted' : color);

    var template = $('#debug-template').text();
    template = template.replace('%%date%%', dateString);
    template = template.replace('%%message%%', message);
    template = template.replace('%%color%%', color);

    $('#files').find('li.empty').fadeOut(); // remove the 'no messages yet'
    $('#files').prepend(template);
}

// Creates a new file and add it to our list
function ui_multi_add_file(id, file)
{
    var template = $('#files-template').text();
    template = template.replace('%%filename%%', file.name);

    template = $(template);
    template.prop('id', 'uploaderFile' + id);
    template.data('file-id', id);

    $('#files').find('li.empty').fadeOut(); // remove the 'no files yet'
    $('#files').prepend(template);
}

// Changes the status messages on our list
function ui_multi_update_file_status(id, status, message)
{
    $('#uploaderFile' + id).find('span').html(message).prop('class', 'status text-' + status);
}

// Updates a file progress, depending on the parameters it may animate it or change the color.
function ui_multi_update_file_progress(id, percent, color, active)
{
    color = (typeof color === 'undefined' ? false : color);
    active = (typeof active === 'undefined' ? true : active);

    var bar = $('#uploaderFile' + id).find('div.progress-bar');

    bar.width(percent + '%').attr('aria-valuenow', percent);
    bar.toggleClass('progress-bar-striped progress-bar-animated', active);

    if (percent === 0) {
        bar.html('');
    }
    else {
        bar.html(percent + '%');
    }

    if (color !== false) {
        bar.removeClass('bg-success bg-info bg-warning bg-danger');
        bar.addClass('bg-' + color);
    }
}