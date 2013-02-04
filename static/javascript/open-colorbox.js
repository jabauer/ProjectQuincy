// This function opens a colorbox window
$(document).ready(function() {
	//hide inline content
	$("a.inline").each(function(i){
		loc = $(this).attr('href');
		w = $(this).attr('width');
		$(this).colorbox({
			inline: 'true',
			href: loc,
			width: w,
			transition:'none',
			overlayClose: 'false',
			onOpen: function( ){
				loc = $(this).attr('href');
				$(loc).toggleClass('hidden');
			},
		});
	});
$(".hidden").hide( );	
});