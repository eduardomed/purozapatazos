var offset = 12

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
            var link = $("<a></a>")
            // console.log(zapatazo["id"])
            // console.log(zapatazo["imglink"])
            $("<img>").attr("src",  zapatazo["imglink"]).attr("alt", "TEST").appendTo(link)
            $(link).attr("href", "/" + zapatazo["id"] + "/").appendTo(tile)
            $('#zapatazos').append(tile)
        }
        
        offset += 12

      }
    });
  });
});