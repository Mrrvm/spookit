
$('.category-button').addClass(function( index ) {
  return "category-" + index;
  });

$('.category-button').each( function(index) {
  $(this).click( function() {
    this_text = $(this).find("p").text();
    console.log("Nome da categoria: " + this_text);
    $( '.button-container' ).slideUp( "fast", function() {
    // Animation complete.
    });

    $.get( "http://172.17.108.101:9000/stories", { theme: "cultura"} )
  .done(function( data ) {
    console.log( "Data Loaded: " + data );
    });

    $('.thread-container_text').text(this_text);
    $('.thread-container').removeClass("hidden");
  });

});

$( '.back-button' ).click(function() {
  $('.thread-container').addClass("hidden");
  $('.button-container').slideDown( "fast", function(){
  });

});

$(document).ready(function() {

});
