/**
 * Created by Zach on 3/6/2015.
 */

$(function() {

    //$('#loginModal').modal({
    //    show: false
    //});//modal

    $('#showLoginModal').on('click', function() {
        //$('#loginModal').modal('show');
        $.ajax({
            url: '/homepage/login.loginform',
            success: function(data) {
                $('#loginModal').find('.modal-content').html(data);
            }
        })

    }); //login btn click



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
                    $('#id_username').after('<span id="id_username_message text-white"><i class="text-white fa fa-check fa-lg"></i></span>');
                }else{ //Invalid UN
                    $('#id_username').after('<span id="id_username_message text-white"><i class="text-white fa fa-times fa-lg"></i></span>');
                }
            } //success
        }); //ajax

    }); //username change

    //$('#loginForm').ajaxForm(function(data) { //Ajax form
    //    $('#loginFormContainer').find('.modal-content').html(data);
    //});



}); //ready
