/**
 * Created by Zach on 3/6/2015.
 */

$(function() {

    $('#id_username').change(function() {
        //var username = $('#id_username');
        var username = $(this).val();
        //console.log(username);
        $.ajax({
            url: '/homepage/login.check_username/',
            type: 'POST',
            data: {
                'u': username
            }, //data
            success: function(resp) {
                $(console.log(resp + ' response'));
                $('#id_username_message').remove();
                if (resp == '1') { //Valid UN
                    $('#id_username').after('<span id="id_username_message"><i class="fa fa-check fa-lg"></i></span>');
                }else{ //Invalid UN
                    $('#id_username').after('<span id="id_username_message"><i class="fa fa-times fa-lg"></i></span>');
                }
            } //success
        }); //ajax

    }); //username change

    $('#loginForm').ajaxForm(function(data) { //Ajax form
        $('#loginModal').find('.modal-content').html(data);
    });





}); //ready
