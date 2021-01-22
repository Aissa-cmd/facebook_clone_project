$(document).ready(function () {
    $(".create_new_account_btn").on("click", function (e) {
        e.preventDefault();
        $('.register_form_wrapper').css('display', 'block');
    });
    // $('.register_form_wrapper').on('click', function(e) {
    // 	$(this).css('display', 'none');
    // });
    // $('.register_form_container').on('click', function(e) {
    // 	if(e.stopPropagation) {
    // 		e.stopPropagation()
    // 	} else {
    // 		e.cancelBubble = true;
    // 	}
    // });
    $('.header_right').on('click', function(e) {
        $('.register_form_wrapper').css('display', 'none');
    });
    $('.register_form_wrapper').on('click', function(e) {
    	$(this).css('display', 'none');
    })
    $('.register_form_container').on('click', function(e) {
    	if(e.stopPropagation) {
    		e.stopPropagation()
    	} else {
    		e.cancelBubble = true;
    	}
    })
});
