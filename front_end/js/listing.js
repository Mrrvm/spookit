$('.category-button').each(function(){
    //if statement here
    // use $(this) to reference the current div in the loop
    //you can try something like...
  var i=0;


  i=i+1;
});

$('.category-button').addClass(function( index ) {
  return "category-" + index;
  });

$('.category-button').each( function(index) {
    $(this).click( function() {
      $( '.row' ).fadeOut( "slow", function() {
      // Animation complete.
      });
    });

});

$(document).ready(function() {

});
