$(document).ready(function () {
    $('.option_hover').on("mouseover", function(e){
    	const module_top = parseInt($('.navbar').css('height')) + 2; 
    	$('.option_info_module').text($(this).attr('data-icon-name'));
    	$('.option_info_module').css('top', module_top);
    	let module_left = this.getBoundingClientRect().left;
        // if(module_left + parseInt($('.option_info_module').css('width')) > widow.innerWidth) {
        //     $('.option_info_module').css('right', "15");
        // } else {
        //     $('.option_info_module').css('left', module_left);
        // }
        $('.option_info_module').css('left', module_left);
    	$('.option_info_module').css('display', 'block');
    })
    $('.option_hover').on('mouseleave', function(e) {
    	$('.option_info_module').css('display', 'none');
    })

    $(".right_options_menu").on("click", function(e) {
        $(".nav_right_options_module").css("display" : "block");
    })
    // $('.post_options_list').on('click', function() {
    //     console.log('click');
    //     $('.post_options_list_module').css('display', 'block');
    //     $('.post_options_list_module').css('top', this.getBoundingClientRect().y);
    //     $('.post_options_list_module').css('');
    // })
});
