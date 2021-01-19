$(document).ready(function () {
    $('.option_hover').on("mouseover", function(e){
    	const module_top = parseInt($('.navbar').css('height')) + 2;
    	$('.option_info_module').text($(this).attr('data-icon-name'));
    	$('.option_info_module').css('top', module_top);
    	let module_left = this.getBoundingClientRect().left;
    	$('.option_info_module').css('left', module_left);
    	$('.option_info_module').css('display', 'block');
    })
    $('.option_hover').on('mouseleave', function(e) {
    	$('.option_info_module').css('display', 'none');
    })
});
