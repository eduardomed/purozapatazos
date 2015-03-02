var offset = 3

$(document).ready(function() {
  $("#driver").click(function(event){
      $.ajax({ url : '/load_more.json', 
        data : {"offset" : offset},
        success: function(jd) {
        // console.log(jd)
        // console.log(jd["Zapatazo"])
        for (var index in jd["Zapatazo"]){
            var zapatazo = jd["Zapatazo"][index]
            var tile = $("<div></div>").addClass("col-md-3")
            $("<img>").attr("src",  zapatazo["imglink"]).attr("alt", zapatazo["title"]).appendTo(tile)
            $('#zapatazos').append(tile)
        }
        
        offset += 3

      }
    });
  });
});