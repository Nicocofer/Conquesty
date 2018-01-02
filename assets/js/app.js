// $( ".planet" ).click(function() {

// 	console.log('Planète de '+this.id);

// 	$("#planetebox").html('<div class="Pdescription"></div>');
// 	$(".Pdescription").html('<div id="close"></div>');

// 	alert('truc');

// });

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