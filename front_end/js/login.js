$.post( "http://172.17.108.101:9000/stories", {user: "username"} )
.done(function( data ) {
  console.log( "Data Loaded: " + data );
  });

$.post( "http://172.17.108.101:9000/stories", {password: "password"} )
.done(function( data ) {
  console.log( "Data Loaded: " + data );
  });

$.post( "http://172.17.108.101:9000/stories", {email: "email"} )
.done(function( data ) {
  console.log( "Data Loaded: " + data );
  });

$( '.back-button' ).click(function() {
  $('.thread-container').addClass("hidden");
  $('.button-container').slideDown( "fast", function(){
  });

});

$(document).ready(function() {

});
