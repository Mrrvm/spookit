$('.category-button').each( function(index) {
  $(this).click( function() {
    this_text = $(this).find("p").text();
    console.log("Nome da categoria: " + this_text);
    $( '.button-container' ).slideUp( "fast", function() {
    });

  $.get( "http://172.17.108.101:9000/stories", { theme: this_text }).done(function( data ) {
	  var json_obj = $.parseJSON(data);
    for (var i in json_obj) {
      $('.thread-links').append('<div class="thread-item" id="item-' + i + '"></div>');
      $('#item-' + i).append('<a href="thread.html#' + json_obj[i].name + '">' + json_obj[i].name + '</a>');
      $('#item-' + i).append('<p> Criado por: ' + json_obj[i].user + ' a ' + json_obj[i].date + '</a>');
    }
  });

    $('.thread-container_text').text(this_text);
    $('.thread-container').removeClass("hidden");
  });

});

$( '.back-button' ).click(function() {
  $('.thread-container').addClass("hidden");
  $('.thread-links').empty();
  $('.button-container').slideDown("fast", function(){
  });

});

$(document).ready(function() {

});
