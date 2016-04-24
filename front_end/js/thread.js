$(document).ready(function() {
  var ttitle = window.location.hash.substr(1);
  var audios;
  var audio_users;
  $.get( "http://172.17.108.101:9000/story", { title: ttitle}).done(function( data ) {
    console.log(data);
	  var json_obj = $.parseJSON(data);//parse JSON
    for (var i in json_obj) {
      if(i == 0) {
        $('.main-thread').append('<h1>' + json_obj[i].name + '</h1>');
        $('.main-thread').append('<p>Criado por:<a href="profile#' + json_obj[i].user + '">' + json_obj[i].user + '</p>')
          audios = json_obj[i].audios;

        for (var k in audios) {
          console.log(audios[k]);
        }

        audio_users = json_obj[i].audio_users;
        $('.main-thread').append('<h2>Contribuidores:</h2>')
        $('.main-thread').append('<ul id="contributor-list"></ul>');
        for (var h in audio_users) {

          $('#contributor-list').append('<li><a href="profile#' + audio_users[h] + '">' + audio_users[h] + '</li>')
        }
      } else {
        if(json_obj[i].comments != "None") {
          for ( var f in json_obj[i].comments) {
            $('.single-thread-container').append('<div class="comment" id= "commentn-' + f +'"></div>');
            $("#commentn-" + f).append('<p><a href="profile#"' + json_obj[i].comments[f].user + '>' + json_obj[i].comments[f].user + '</a> respondeu:</p>');
            $("#commentn-" + f).append('<p>' + json_obj[i].comments[f].comment + '</p>');
            $("#commentn-" + f).append('<p class="time">' + json_obj[i].comments[f].date + '</p>');
          }
        }
      }
    }
  });

});

