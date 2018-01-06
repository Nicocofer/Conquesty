

$( ".planet" ).click(function() {

	n = '#p'+this.id ;

	$(".boxP").css('display','none');
	$(n).css('display','flex');
});

function openbox() {
   $(".Pdescription").css("display","flex");
   // $(".planet").css("display","none");
   console.log(this);
}

function closebox() {
     $(".Pdescription").css('display','none');
     // $(".planet").css("display","flex");
}

closebox();
