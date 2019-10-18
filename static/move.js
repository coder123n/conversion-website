$(document).ready(function(){
	$("#d2").hide();
	$("#d1").click(function(){
		$("#d2").show();
		$("#d1").hide();
	});
	$("#d2").click(function(){
		$("#d1").show();
		$("#d2").hide();
	});
	
	$("#kr").click(function(){
		$("#kr").move();
});