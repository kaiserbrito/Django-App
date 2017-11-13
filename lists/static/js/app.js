$(function () {
    $(".js-add-user").click(function() {
        $.ajax({
            url: '/lists/create/',
            type: 'get',
            dataType: 'json',
            success: function(data) {
                $("#add-user-content").html(data.html_form);
            }
        });
    });
});