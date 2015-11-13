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

    // $('#zapatazoModal').on('show.bs.modal', function(event) {
    //     openModal(event)
    // })

});
    
function loadMore(){
      $.ajax({ url : '/load_more.json', 
        data : {"offset" : offset},
        success: function(jd) {
        // console.log(jd)
        // console.log(jd["Zapatazo"])
        for (var index in jd["Zapatazo"]){
            var zapatazo = jd["Zapatazo"][index];
            var tile = $("<div></div>").addClass("col-md-3").addClass("col-sm-6");
            var link = $("<a></a>").attr("href",zapatazo["id"]).attr("target","_blank");
            $("<img>").attr("src",  zapatazo["imglink"]).attr("alt", zapatazo["id"] ).appendTo(link);
            $(link).appendTo(tile);
            $('#zapatazos').append(tile);
        }
      }
    });
}


// function openModal(event){
//     console.log("in the event handler");
//     var button = $(event.relatedTarget) // Button that triggered the modal

//     // Extract info from data-* attributes
//     var zapatazoID = button.data('zapatazo-id') 
//     var zapatazoImage = button.data('zapatazo-img') 

//     var modal = $("#zapatazoModal")
//     modal.find("#zapatazo-modal-img").attr('src', zapatazoImage)
//     modal.find("#zapatazo-modal-link").attr('href', "/" + zapatazoID)
//     modal.find(".twitter-hashtag-button").attr('data-url', "http://zapatazos.herokuapp.com/" + zapatazoID);
// }
  
