$(document).ready(function () {
    $(".create_new_account_btn").on("click", function (e) {
        e.preventDefault();
        $('.register_form_wrapper').css('display', 'block');
    });
    $('.header_right').on('click', function(e) {
        $('.register_form_wrapper').css('display', 'none');
    })
});
