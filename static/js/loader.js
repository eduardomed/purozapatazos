var offset = 12

$(document).ready(function() {
    $(window).scroll(function(){
        var wintop = $(window).scrollTop(), docheight = $(document).height(), winheight = $(window).height();
        var  scrolltrigger = 0.99;
 
        if  ((wintop/(docheight-winheight)) > scrolltrigger) {
         console.log('scroll bottom');
         loadMore();
         offset += 12
        }
    });

    $('#zapatazoModal').on('show.bs.modal', function(event) {
        openModal(event)
    })

});
    
function loadMore(){
      $.ajax({ url : '/load_more.json', 
        data : {"offset" : offset},
        success: function(jd) {
        // console.log(jd)
        // console.log(jd["Zapatazo"])
        for (var index in jd["Zapatazo"]){
            var zapatazo = jd["Zapatazo"][index]
            var tile = $("<div></div>").addClass("col-md-3")
            var link = $("<a></a>").attr("data-toggle", "modal")
                                    .attr("data-target", "#zapatazoModal")
                                    .data("zapatazo-id", zapatazo["id"])
                                    .data("zapatazo-img", zapatazo["imglink"])
            $("<img>").attr("src",  zapatazo["imglink"]).attr("alt", zapatazo["id"] ).appendTo(link)
            $(link).appendTo(tile)
            $('#zapatazos').append(tile)
        }
      }
    });
}


function openModal(event){
    console.log("in the event handler")
    var button = $(event.relatedTarget) // Button that triggered the modal

    // Extract info from data-* attributes
    var zapatazoID = button.data('zapatazo-id') 
    var zapatazoImage = button.data('zapatazo-img') 

    // If necessary, you could initiate an AJAX request here (and then do the updating in a callback).
    // Update the modal's content. We'll use jQuery here, but you could use a data binding library or other methods instead.
    var modal = $("#zapatazoModal")
    modal.find("#zapatazo-modal-img").attr('src', zapatazoImage)
    modal.find("#zapatazo-modal-link").attr('href', "/" + zapatazoID)
}
  
