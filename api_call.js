$(document).ready(function(){

$("#filter_button").click(function () {
                movie_name = this.value
                $.ajax({ url: "http://127.0.0.1:8000/shows/" + $("#date_filter").val(),
                success: function(result){
                  $("#theatre").html("")
                   movies_div = "<h2>Movies whose shows are on or after the selected date</h2>"
                   $.each(result, function(index) {
                    movies_div += "<input type='button' class=movie_list  id="+ result[index].id +" value="+ result[index].name + "><br><br>"
                    });
                    $("#movies").html(movies_div)


                $(".movie_list").click(function () {
                movie_name = this.value
                $.ajax({ url: "http://127.0.0.1:8000/shows/" + this.id,
                success: function(result){

                  // Movie buttons listing
                  $("#theatre").html("")
                   theatre_div = "<h3>Theatres shows for " + movie_name +" movie</h3>"
                   theatre_div += "<table border=1 cell=1><th>Theatre Name</th><th>Show Starts at</th><th>Show Ends at</th>"
                   $.each(result, function(index) {
                    theatre_div += "<tr> <td>"+ result[index].screen.theatre.name + "</td> <td>" + result[index].start+ "</td> <td>" + result[index].end + "</td> <tr>"
                    });
                    theatre_div += "</table>"
                    $("#theatre").html(theatre_div)
                    }
                });
                });
                    }
                });
            });





    $.ajax({ url: "http://127.0.0.1:8000",
        success: function(result){
           movies_div = "<h2>Movies Listing</h2>"
           $.each(result, function(index) {
            movies_div += "<input type='button' class=movie_list  id="+ result[index].id +" value="+ result[index].name + "><br><br>"
            });
            $("#movies").html(movies_div)


            $(".movie_list").click(function () {
                movie_name = this.value
                $.ajax({ url: "http://127.0.0.1:8000/shows/" + this.id,
                success: function(result){

                  // Movie buttons listing
                  $("#theatre").html("")
                   theatre_div = "<h3>Theatres shows for " + movie_name +" movie</h3>"
                   theatre_div += "<table border=1 cell=1><th>Theatre Name</th><th>Show Starts at</th><th>Show Ends at</th>"
                   $.each(result, function(index) {
                    theatre_div += "<tr> <td>"+ result[index].screen.theatre.name + "</td> <td>" + result[index].start+ "</td> <td>" + result[index].end + "</td> <tr>"
                    });
                    theatre_div += "</table>"
                    $("#theatre").html(theatre_div)
                    }
                });
            });
        }
    });
});