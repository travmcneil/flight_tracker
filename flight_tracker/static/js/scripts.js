$(document).ready(function(){
    console.log("working");
})

var from_text = $("#from_text").val();
$("#from_text").change(function(){
    var from_text = $("#from_text").val();
    console.log(from_text);
});

var to_text = $("#to_text").val();
$("#to_text").change(function(){
    var to_text = $("#to_text").val();
    
    console.log(to_text);
});

