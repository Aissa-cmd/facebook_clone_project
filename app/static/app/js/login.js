$(document).ready(function () {
	function create_error(error_msg) {
		const elem = document.createElement('li');
		elem.textContent = error_msg;
		return elem
	}
    $(".create_new_account_btn").on("click", function (e) {
        e.preventDefault();
        $('.register_form_wrapper').css('display', 'block');
    });
    $('.header_right').on('click', function(e) {
        $('.register_form_wrapper').css('display', 'none');
    });
    $('label').on('click', function(e) {
    	e.preventDefault();
    });
});
