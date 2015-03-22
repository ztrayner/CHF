/**
 * Created by Zach on 3/6/2015.
 */

$(function() {
 console.log("hey");

    $('.add_to_cart').on('click', function() {

    console.log("clicked");
    var pid = $(this).attr('data-pid');
    // var qty = ;

    $.loadmodal({
        url:"/homepage/cart.add/" + pid,
        title: 'Shopping Cart',
        width: '700px'
    });


});

});//ready
