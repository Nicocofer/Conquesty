$( ".planet" ).click(function() {

	n = '#p'+this.id ;

	$(".boxP").css('display','none');
	$(n).css('display','flex');
	console.log(n);

});

// $('#close').click(function(){
// 		$(".Pdescription").css('display','none');
// 		$("#planetebox").html('<div class="planet" id="type0"></div><div class="planet" id="type1"></div><div class="planet" id="type2"></div><div class="planet" id="type3"></div>');
		


// 	});


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