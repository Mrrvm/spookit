function showData() {
        $.ajax({
            type: 'POST',
            url: 'example.aspx/GetData',
            contentType: 'application/json; charset=utf-8',
            dataType: 'json',
            success: function (msg) {

                var table = '<thead><tr><td>ID</td><td>COMPANY</td>' +
            '<td>ADDRESS</td><td>Edit</td><td>Delete</td></tr></thead><tbody>';
                // loop each record
                for (var i = 0; i < msg.d.length; i++) {
                    table += '<tr><td>' + msg.d[i].ID + '</td>' +
                              '<td>' + msg.d[i].name+ '</td><td>' + msg.d[i].ADDRESS + '</td>' +
                              '<td><button type="button" class="edit">Edit</button></td>' +
                              '<td><button type="button" class="delete">Delete</button></td></tr>';

                }
                table += '</tbody>';
               $('#example').html(table).dataTable();




            }

        })


}
