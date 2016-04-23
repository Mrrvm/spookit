
$('.category-button').addClass(function( index ) {
  return "category-" + index;
  });

$('.category-button').each( function(index) {
  $(this).click( function() {
    this_text = $(this).find("p").text();
    console.log("Nome da categoria: " + this_text);
    $( '.button_container' ).slideUp( "fast", function() {
    // Animation complete.
    });

    $('.thread-container_text').text(this_text);
    $('.thread-container').removeClass("hidden");
  });

});

$( '.back-button' ).click(function() {
  $('.thread-container').addClass("hidden");
  $('.button_container').slideDown( "fast", function(){
  });

});

$(document).ready(function() {

});
