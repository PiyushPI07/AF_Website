jQuery.noConflict();
import $ from 'jquery.js'

window.onorientationchange = function(event) {
	window.location.reload(); 
	console.log("Orientation changed")
}
$(document).bind('ready', function() {
	var docScroll = $(document).scrollTop()
	var big_logo_pos = document.getElementById("landing-image").getBoundingClientRect()
	var nav_logo_pos = document.querySelector("#header .logo").getBoundingClientRect()
	if(docScroll > 0){
		console.log(big_logo_pos, nav_logo_pos)
		if(window.screen.width < 767){
			$('#landing-image').css({
				width: "65px",
				height: "65px",
				transform: "translate(calc("+ ((nav_logo_pos.x+65/2) - (big_logo_pos.x+big_logo_pos.width/2)) +"px), calc("+((nav_logo_pos.y+65/2) - (big_logo_pos.y+big_logo_pos.height/2))+"px))",
			})
		}
		else{
			$('#landing-image').css({
				width: "65px",
				height: "65px",
				transform: "translate(calc("+ ((nav_logo_pos.x+65/2) - (big_logo_pos.x+big_logo_pos.width/2)) +"px), calc("+((nav_logo_pos.y+65/2) - (big_logo_pos.y+big_logo_pos.height/2)-docScroll)+"px))",
			})
		}
		console.log("translate(calc("+ ((nav_logo_pos.x+65/2) - (big_logo_pos.x+big_logo_pos.width/2)) +"px), calc("+((nav_logo_pos.y+65/2) - (big_logo_pos.y+big_logo_pos.height/2)-docScroll)+"px))")
		$('body').css({overflow: "visible"})
		$('#slider-button').css({visibility: "hidden", opacity: 0})
		$('#landing-heading').css({visibility: "hidden", opacity: 0})
		$('#header .logo').append('<img alt="Logo" src="{% static "images/af.png" %}" style="width: 65px;">')
		$('.header-animate .logo').append('<img alt="Logo" src="{% static "images/af.png" %}" style="width: 65px;">')
	}
	else{
		$('body').css({overflow: "hidden"})
	}
})
function transform() {
	var big_logo_pos = document.getElementById("landing-image").getBoundingClientRect()
	var nav_logo_pos = document.querySelector("#header .logo").getBoundingClientRect()
	if(!$('#landing-image').hasClass("landing-effect")){
		$('body').css({overflow: "visible"})
		$('#landing-image').addClass("landing-effect").css({
			width: "65px",
			height: "65px",
			transform: "translate(calc("+ ((nav_logo_pos.x+65/2) - (big_logo_pos.x+big_logo_pos.width/2)) +"px), calc("+((nav_logo_pos.y+65/2) - (big_logo_pos.y+big_logo_pos.height/2))+"px))",
		})
		$('#slider-button').css({visibility: "hidden", opacity: 0})
		$('#landing-heading').css({visibility: "hidden", opacity: 0})
		setTimeout(function () {
			$('#header .logo').append('<img alt="Logo" src="{% static "images/af.png" %}" style="width: 65px;">')
			$('.header-animate .logo').append('<img alt="Logo" src="{% static "images/Logo.png" %}" style="width: 65px;">')
			$('#landing-image').css({visibility: "hidden"})
			window.scrollBy(0, 700)
		}, 500)
	}
}
$(document).bind('scroll', function(){
	var docScroll = $(document).scrollTop()
	var big_logo_pos = document.getElementById("landing-image").getBoundingClientRect()
	var nav_logo_pos = document.querySelector("#header .logo").getBoundingClientRect()
	if($('.slider').length && docScroll){
		// Triggers when scrolled            
	}
	else{
		// Triggers when top is hit
		$('body').css({overflow: "hidden"})
		$('#header .logo img').remove()
		if(window.screen.width < 767){
			$('#landing-image').css({
				visibility: "visible",
				transform: "translate(calc("+ (-(nav_logo_pos.x+65/2) + (big_logo_pos.x+big_logo_pos.width/2)) +"px), calc("+(-(nav_logo_pos.y+65/2) + (big_logo_pos.y+big_logo_pos.height/2))+"px))",
				height: "200px",
				width: "200px"
			}).removeClass("landing-effect")
		}
		else{
			$('#landing-image').css({
				visibility: "visible",
				transform: "translate(calc("+ (-(nav_logo_pos.x+65/2) + (big_logo_pos.x+big_logo_pos.width/2)) +"px), calc("+(-(nav_logo_pos.y+65/2) + (big_logo_pos.y+big_logo_pos.height/2))+"px))",
				height: "300px",
				width: "300px"
			}).removeClass("landing-effect")
		}
		$('#slider-button').css({visibility: "visible", opacity: 1})
		$('#landing-heading').css({visibility: "visible", opacity: 1})
	}
})