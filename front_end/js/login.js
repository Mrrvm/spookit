$( '.e-submit-form' ).click(function() {
  var user;
  var pass;

  user = $('.login_name').val();
  pass = $('.login_pass').val();
  console.log(user);
  console.log(pass);

  $.post( "http://172.17.108.101:9000/users", { user: user , log_type: "1" , password: pass}).done(function( data ) {
	  var json_obj = $.parseJSON(data);
  });

});

$(document).ready(function() {
  console.log("Page loaded");
});

$( '.r-submit-form' ).click(function() {
  var user;
  var pass;
  var email;
  var conf_pass;

  user = $('.r-email').val();
  pass = $('.r-pass').val();
  conf_pass = $('.r-confirm-pass').val();
  email =  $('.r-email').val();
  console.log(user);
  console.log(pass);
  console.log(email);


  if( pass == conf_pass ) {
    // PUTS
  } else {
    alert("Passwords do not match");
  }

});

$(document).ready(function() {
  console.log("Page loaded");
});
