function openbox(){$(".Pdescription").css("display","flex")}function closebox(){$(".Pdescription").css("display","none")}$(".planet").click(function(){n="#p"+this.id,$(".boxP").css("display","none"),$(n).css("display","flex")}),$("#menuinfos").click(function(){$(".bodyP").css("display","flex"),$(".bodyC").css("display","none")}),$("#menuconstruire").click(function(){$(".bodyP").css("display","none"),$(".bodyC").css("display","flex")});