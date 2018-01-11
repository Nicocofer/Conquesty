// Partie qui gère l'ouverture de la fenêtre au clic sur une planète

$( ".planet" ).click(function() {

	n = '#p'+this.id ;

	$(".boxP").css('display','none');
	$(n).css('display','flex');
	
});

function openbox() {
   $(".Pdescription").css("display","flex");
   // $(".planet").css("display","none");

}

// Partie qui ferme la fenetre Pdescription -> description de la planète

function closebox() {
     $(".Pdescription").css('display','none');
     // $(".planet").css("display","flex");
}

// Partie menu du bas de la page descritpion planète 

$( "#menuinfos" ).click(function() {

	$(".bodyP").css('display','flex');
	$(".bodyC").css('display','none');

});

$( "#menuconstruire" ).click(function() {

	
	$(".bodyP").css('display','none');
	$(".bodyC").css('display','flex');
	
	
});
