/**
 * Created by leonid <> on 23.11.14.
 */
$("#youtube").autocomplete({
    source: function(request, response) {
        var apiKey = 'AIzaSyA2KQaiWRK_l_t1asGzg6rvv0gKpM6DdFA';
        var query = request.term;
        $.ajax({
            url: "http://suggestqueries.google.com/complete/search?hl=en&ds=yt&client=youtube&hjson=t&cp=1&q=" + query + "&key=" + apiKey + "&format=5&alt=json&callback=?",
            dataType: 'jsonp',
            success: function(data, textStatus, request) {
                $.youtubeAPI(data[1][0][0]);
            }
        });
    }
});
$.youtubeAPI = function(kelime) {
    $('#spinner').show();
    $('#sonuc').css({opacity: 0.2});
    $.ajax({
        type: 'GET',
        url: 'http://gdata.youtube.com/feeds/api/videos?q=' + kelime + '&max-results=5&v=2&alt=jsonc',
        dataType: 'jsonp',
        success: function(veri) {
            $('#spinner').hide();
            $('#sonuc').empty();
            $('#sonuc').css({opacity: 1.0});
            $.each(veri.data.items, function(i, data) {
                $.youtubeAppend(data.id, "sonuc");
            });
        }
    });
}
$.youtubePlay = function(yid) {
    $.ajax({url: '/api/add_video/' + party_token + "/" + yid + "/" + user_token + "/"})
}
